"""Search for RecSys 2025 papers via Playwright/Chromium — no API key needed.

Strategy:
  1. Try arXiv title search (free, direct PDF links).
  2. Fall back to Semantic Scholar open-access API.
  3. Download found PDFs; log failures for manual retrieval.
"""

import asyncio
import json
import re
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Optional

from playwright.async_api import Page, async_playwright

ARTICLES_DIR = Path("research_results/articles")
FAILURES_FILE = Path("research_results/search_failures_browser.md")
ARTICLES_DIR.mkdir(parents=True, exist_ok=True)


def load_titles(md_path: str) -> list:
    """Parse paper titles from the markdown table in recsys_2025.md."""
    titles = []
    with open(md_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if (
                line.startswith("|")
                and not line.startswith("| Title")
                and not line.startswith("|---")
            ):
                parts = line.split("|")
                if len(parts) >= 2:
                    title = parts[1].strip()
                    if len(title) > 10:
                        titles.append(title)
    return titles


def clean_filename(title: str) -> str:
    """Strip characters illegal in filenames and cap length."""
    return re.sub(r'[\\/*?:"<>|]', "", title)[:80]


def download_pdf(url: str, dest: Path) -> bool:
    """Fetch a PDF from url and save to dest; returns False if not a real PDF."""
    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                )
            },
        )
        with urllib.request.urlopen(req, timeout=25) as resp:
            data = resp.read()
        if data[:4] != b"%PDF":
            return False
        dest.write_bytes(data)
        return True
    except OSError as e:
        print(f"    Download error: {e}")
        return False


async def search_arxiv(page: Page, title: str) -> Optional[str]:
    """Search arXiv by title and return the PDF URL of the first result."""
    query = urllib.parse.quote(f'ti:"{title}"')
    url = f"https://arxiv.org/search/?searchtype=ti&query={query}&start=0"
    await page.goto(url, timeout=30000)
    await page.wait_for_load_state("domcontentloaded")

    result = await page.query_selector("li.arxiv-result p.list-title a")
    if not result:
        return None
    abs_url = await result.get_attribute("href")
    if not abs_url:
        return None
    pdf_url = abs_url.replace("/abs/", "/pdf/")
    if not pdf_url.endswith(".pdf"):
        pdf_url += ".pdf"
    return pdf_url


async def search_semantic_scholar(page: Page, title: str) -> Optional[str]:
    """Return open-access PDF URL from Semantic Scholar API, or None."""
    query = urllib.parse.quote(title)
    api_url = (
        "https://api.semanticscholar.org/graph/v1/paper/search"
        f"?query={query}&limit=1&fields=title,openAccessPdf"
    )
    await page.goto(api_url, timeout=30000)
    await page.wait_for_load_state("domcontentloaded")
    try:
        data = json.loads(await page.inner_text("body"))
        papers = data.get("data", [])
        if papers and papers[0].get("openAccessPdf"):
            return papers[0]["openAccessPdf"].get("url")
    except (json.JSONDecodeError, KeyError):
        pass
    return None


async def find_pdf_url(page: Page, title: str) -> Optional[str]:
    """Try arXiv then Semantic Scholar; return first PDF URL found."""
    try:
        url = await search_arxiv(page, title)
        if url:
            return url
    except Exception as e:  # network / timeout errors
        print(f"    arXiv error: {e}")

    try:
        url = await search_semantic_scholar(page, title)
        if url:
            return url
    except Exception as e:
        print(f"    Semantic Scholar error: {e}")

    return None


async def main() -> None:
    """Main entry point: search and download all missing papers."""
    titles = load_titles("sources/recsys_2025.md")
    print(f"Found {len(titles)} paper titles.")

    failed: list = []
    downloaded: list = []

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            )
        )
        page = await context.new_page()

        for i, title in enumerate(titles, 1):
            dest = ARTICLES_DIR / f"{clean_filename(title)}.pdf"

            if dest.exists():
                print(f"[{i}/{len(titles)}] Skip (exists): {title[:55]}")
                continue

            print(f"[{i}/{len(titles)}] Searching: {title[:60]}...")
            pdf_url = await find_pdf_url(page, title)

            if pdf_url:
                print(f"    URL: {pdf_url}")
                if download_pdf(pdf_url, dest):
                    print("    -> Downloaded OK")
                    downloaded.append(title)
                else:
                    print("    -> Download failed (bad PDF or redirect)")
                    failed.append(title)
            else:
                print("    -> Not found (likely ACM-paywalled)")
                failed.append(title)

            await asyncio.sleep(2)

        await browser.close()

    FAILURES_FILE.write_text(
        "# Papers not found or failed to download (browser search)\n\n"
        + "".join(f"- {t}\n" for t in failed),
        encoding="utf-8",
    )
    print(f"\nDone. Downloaded: {len(downloaded)}, Failed: {len(failed)}")
    print(f"Failures logged to {FAILURES_FILE}")


if __name__ == "__main__":
    asyncio.run(main())

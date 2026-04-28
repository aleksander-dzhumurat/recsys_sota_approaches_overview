import os
import re
import urllib.request
from duckduckgo_search import DDGS
import time

os.makedirs('research_results/articles', exist_ok=True)

with open('sources/recsys_2025.md', 'r') as f:
    text = f.read()

titles = []
for line in text.split('\n'):
    line = line.strip()
    if line.startswith('|') and not line.startswith('| Title') and not line.startswith('|---') and not line.startswith('| Title | Organization |'):
        parts = line.split('|')
        if len(parts) >= 2:
            title = parts[1].strip()
            if title and len(title) > 10:
                titles.append(title)

print(f"Found {len(titles)} titles. Starting web search (this will take a while)...")

failed = []
downloaded = []

ddgs = DDGS()

for title in titles:
    clean_title = re.sub(r'[\\/*?:"<>|]', "", title)
    filename = f"research_results/articles/{clean_title[:80]}.pdf"
    
    if os.path.exists(filename):
        print(f"[{title[:40]}] Already exists locally. Skipping.")
        continue

    print(f"Searching web for: {title[:40]}...")
    
    query = f'"{title}"'
    
    pdf_url = None
    try:
        # Get top 5 results
        results = list(ddgs.text(query, max_results=5))
        
        for res in results:
            url = res.get('href', '')
            
            # Arxiv conversion
            if 'arxiv.org/abs/' in url:
                pdf_url = url.replace('/abs/', '/pdf/')
                if not pdf_url.endswith('.pdf'):
                    pdf_url += '.pdf'
                break
            elif url.endswith('.pdf'):
                pdf_url = url
                break
                
    except Exception as e:
        print(f"  Search error: {e}")

    if pdf_url:
        print(f"  Found PDF link: {pdf_url}")
        try:
            req = urllib.request.Request(pdf_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
            with urllib.request.urlopen(req, timeout=15) as response, open(filename, 'wb') as out_file:
                out_file.write(response.read())
            print("  -> Downloaded successfully.")
            downloaded.append(title)
        except Exception as e:
            print(f"  Download error: {e}")
            failed.append(title)
    else:
        print("  -> No PDF link found in top results.")
        failed.append(title)
        
    time.sleep(2) # delay to avoid blocking

# Write failures
with open('research_results/search_failures.md', 'w') as f:
    f.write("# Papers not found or failed to download\n\n")
    for t in failed:
        f.write(f"- {t}\n")

print(f"Done! Downloaded {len(downloaded)} new papers, {len(failed)} failed searches to be manually checked.")

# Literature Scraping & Download Plan

## Overall Objective
Automate the mass-downloading of academic papers listed in `sources/recsys_2025.md` to enrich our local research knowledge base, while handling failures gracefully.

## Strategy Logic

1. **Title Extraction**: 
   Read the `sources/recsys_2025.md` file locally and parse out the data. Rather than using fixed indices, the script looks for markdown table formats and dynamically extracts the strings that represent paper titles, filtering out headers and empty strings.

2. **Deduplication Check**: 
   Before performing any web requests, map the title to a clean filename format and check the `research_results/articles/` directory. If the PDF already exists, skip it to save time, avoid API rate limits, and preserve bandwidth.

3. **Programmatic Query Execution**: 
   For each missing paper, utilize an external web querying utility (like DuckDuckGo's programmatic search) to execute a targeted web query.

4. **Iterative Result Inspection**: 
   - Extract the top returned links for the query.
   - Look for standard patterns indicating academic PDFs. Specifically, check if the link ends in `.pdf`.
   - Check if the link points to a common preprint repository like arXiv (e.g., `arxiv.org/abs/...`). If it does, automatically translate the abstract link to the direct download endpoint (e.g., `arxiv.org/pdf/...`).

5. **Download Pipeline**: 
   - Once a definitive PDF link is identified, initialize an HTTP request to proxy the download. 
   - Apply timeouts and appropriate user-agents to bypass rudimentary bot-protections.
   - If the request is successful, write the resulting binary data directly into `research_results/articles/[Title].pdf`.

6. **Rate Limiting and Throttling**:
   Pause execution briefly between every individual query and download to avoid IP bans and shadow-blocking from search engines and hosting platforms.

7. **Error Handling & Failure Logging**: 
   - Wrap the network requests (both searching and downloading) in isolated error-handling blocks.
   - Keep a running list of papers that either returned no relevant links or threw download errors.
   - Upon completion, write all unfulfilled titles into `research_results/search_failures.md` so that they can be tracked, investigated, and manually downloaded if necessary (as many papers are paywalled behind ACM Digital Library).

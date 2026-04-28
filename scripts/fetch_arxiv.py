import os
import re
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import time

os.makedirs('research_results/articles', exist_ok=True)

with open('sources/recsys_2025.md', 'r') as f:
    text = f.read()

# Extract titles from markdown tables
titles = []
for line in text.split('\n'):
    line = line.strip()
    if line.startswith('|') and not line.startswith('| Title') and not line.startswith('|---') and not line.startswith('| Title | Organization |'):
        parts = line.split('|')
        if len(parts) >= 2:
            title = parts[1].strip()
            # simple heuristic to avoid short non-titles
            if title and len(title) > 10:
                titles.append(title)

print(f"Found {len(titles)} titles.")

failed = []

for title in titles:
    print(f"Searching for: {title}")
    # clean Title for search
    query = re.sub(r'[^\w\s]', '', title)
    # search using the words
    words = query.split()
    if len(words) > 6:
        words = words[:6] # use first 6 words for broader match
    
    search_query = "+AND+".join(f"all:{urllib.parse.quote(w)}" for w in words)
    url = f'http://export.arxiv.org/api/query?search_query={search_query}&start=0&max_results=1'
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        xml_data = response.read()
        root = ET.fromstring(xml_data)
        
        # namespace for arxiv
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        entries = root.findall('atom:entry', ns)
        
        if entries:
            entry = entries[0]
            # Verify the matched title isn't wildly different
            found_title = entry.find('atom:title', ns).text.replace('\n', ' ')
            
            pdf_url = None
            for link in entry.findall('atom:link', ns):
                if link.attrib.get('title') == 'pdf':
                    pdf_url = link.attrib.get('href')
                    break
            
            if pdf_url:
                clean_title = re.sub(r'[\\/*?:"<>|]', "", title)
                filename = f"research_results/articles/{clean_title[:80]}.pdf"
                
                print(f"  Found PDF on arXiv: {found_title[:50]}...")
                req = urllib.request.Request(pdf_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req) as response, open(filename, 'wb') as out_file:
                    data = response.read()
                    out_file.write(data)
            else:
                print("  No PDF link found.")
                failed.append(title)
        else:
            print("  Not found on arXiv.")
            failed.append(title)
            
    except Exception as e:
        print(f"  Error: {e}")
        failed.append(title)
    
    # 3 second sleep to respect rate limits
    time.sleep(3)

with open('research_results/failed_search.md', 'w') as f:
    f.write("# Failed to Find/Download\n\n")
    for t in failed:
        f.write(f"- {t}\n")

print("Done! Check research_results directory.")

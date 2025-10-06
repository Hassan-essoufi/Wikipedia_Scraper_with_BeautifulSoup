from bs4 import BeautifulSoup
from urllib.parse import urlparse

def parse_html(html_doc):
    return BeautifulSoup(html_doc,'html.parser')

def extract_title(soup):
    title = soup.title
    return title.get_text(strip=True)

def extract_paragraphs(soup):
    paragraphs = soup.find_all('p')
    txt_paragraphs = [p.get_text().strip for p in paragraphs]
    return txt_paragraphs

def extract_internal_links(soup, page_url):
    if page_url:
        parsed = urlparse(page_url)
        base_url = f"{parsed.scheme}://{parsed.netloc}"
    else:
        base_url = "https://fr.wikipedia.org"  # valeur par défaut

    internal_links = []
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        if href.startswith("/wiki/") and not any(x in href for x in [":", "#"]):
            internal_links.append(base_url+href)
    return list(set(internal_links))

def extract_tables(soup):
    tables = []
    for table in soup.find_all("table"):
        tables.append(table.get_text(separator=" ").strip()) 
    return tables 

def build_article_dict(title, url, text, tables, links):
    if isinstance(text, list):
        text = "\n".join(str(p).strip() for p in text if p)

    article_data = {
        "title": str(title).strip() if title else "Untitled",
        "url": url.strip() if url else "",
        "content": text.strip() if isinstance(text, str) else "",
        "tables": tables if tables else [],
        "internal_links": links if links else []
    }

    return article_data



 

from datetime import datetime
from scraper.fetcher import validate_url, validate_page, fetch_page_html, fetch_multiple
from scraper.parser import parse_html, extract_title, extract_paragraphs, extract_internal_links, extract_tables, build_article_dict
from scraper.saver import save_raw_html, save_processed_html


def scrape_single_article(url):
    if validate_url(url) == False:
        print("URL invalide")
        return None
    
    page_valid = validate_page(url)
    if page_valid != True:
        print(f"Page invalide: {page_valid}")
        return None
    
    print("Récupération du contenu...")
    html_content = fetch_page_html(url)
    if not html_content:
        print("Échec de la récupération du HTML")
        return None
    

    filename = f"raw_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    save_raw_html(html_content, filename)
    
    print("Parsing du contenu...")
    soup = parse_html(html_content)
    
    print("Extraction des données...")
    title = extract_title(soup)
    paragraphs = extract_paragraphs(soup)
    links = extract_internal_links(soup,url)
    tables = extract_tables(soup)
    
    article_data = build_article_dict(
        title=title,
        url=url,
        text=paragraphs,
        tables=tables,
        links=links
    )
    
    article_data['metadata'] = {
        'scraped_at': datetime.now().isoformat(),
        'paragraph_count': len(paragraphs) if paragraphs else 0,
        'internal_links_count': len(links) if links else 0,
        'tables_count': len(tables) if tables else 0
    }
    
    print(f" Article scrapé avec succès: {article_data['title']}")
    print(f"{article_data['metadata']['paragraph_count']} paragraphes")
    print(f"{article_data['metadata']['internal_links_count']} liens internes")
    print(f"{article_data['metadata']['tables_count']} tableaux")
    save_processed_html(article_data,filename)
    return article_data


def scrape_multiple(urls):
    articles = []
    success_count = 0
    fail_count = 0
    
    for url in urls:
        article = scrape_single_article(url)
        if article:
            articles.append(article)
            success_count += 1
        else:
            fail_count += 1
            articles.append({
                'url': url,
                'error': 'Scraping failed',
                'metadata': {'scraped_at': datetime.now().isoformat()}
            })
    
    print(f"\nRésumé: {success_count} succès, {fail_count} échecs")
    return articles



def main():
    print("Wikipedia Scraper")
    print("=" * 50)
    nbre_urls = int(input('choisir le nombre des articles à scraper:'))

    if nbre_urls == 1:
        url = input('donner le URL:')
        article = scrape_single_article(url)
        return article
        
    elif nbre_urls >=2:
        urls = []
        for i in range(nbre_urls):
            url = input('donner les URLs:')
            urls.append(url)
        articles = scrape_multiple(urls)
        return articles
    
    else:
        print("Choix invalide")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgramme interrompu par l'utilisateur")
    except Exception as e:
        print(f"Erreur inattendue: {e}")
        import traceback
        traceback.print_exc()
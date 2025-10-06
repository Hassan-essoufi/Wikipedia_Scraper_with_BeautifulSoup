import os
import requests
from bs4 import BeautifulSoup
import re

def validate_url(url):
    pattern = r'^https?://[a-z]{2,3}.wikipedia.org/wiki/[^/?#]+$'
    return bool(re.match(pattern, url))

def validate_page(url):
    is_valid_url = validate_url(url)
    if is_valid_url == False:
        return "Url non valide"
    headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'}
    try :
        response = requests.head(url, allow_redirects=True, timeout=20, headers=headers)
        if response.status_code == 404:
            return False, "Page non trouvée (404)"
        elif response.status_code == 403:
            return False, "Accès interdit (403)"
        elif response.status_code != 200:
            return False, f"Erreur HTTP {response.status_code}"
        return True

    except requests.exceptions.RequestException as e:
        return False, f"Erreur de connexion: {e}"

def fetch_page_html(url):
    if validate_url(url) == True:
        headers = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'
    }
        response = requests.get(url,headers=headers)
        html = response.text
        return html

def fetch_multiple(urls):
    htmls_urls = {}
    headers =  {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64;       x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'
    }  
    for url in urls:
        if validate_page(url) == True:
            response = requests.get(url,headers=headers)
            html = response.text
            htmls_urls[url] = html
    return htmls_urls





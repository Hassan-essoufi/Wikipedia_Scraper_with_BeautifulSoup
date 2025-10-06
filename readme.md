# Wikipedia Scraper avec BeautifulSoup

Ce projet permet d'extraire et de structurer le contenu d'articles Wikipedia en utilisant Python et la bibliothèque BeautifulSoup.

## Fonctionnalités principales

- **Validation d'URL et de page** : Vérifie que l'URL fournie correspond à un article Wikipedia valide et que la page existe.
- **Récupération du HTML** : Télécharge le contenu HTML d'une page Wikipedia.
- **Parsing et extraction** : Utilise BeautifulSoup pour extraire le titre, les paragraphes, les liens internes et les tableaux présents dans l'article.
- **Sauvegarde** : Enregistre le HTML brut et les données structurées (JSON) dans le dossier `data`.
- **Traitement multiple** : Permet de scraper plusieurs articles en une seule commande.

## Structure du projet

- `main.py` : Point d'entrée du projet, gère le workflow principal.
- `scraper/fetcher.py` : Validation et récupération du HTML des pages Wikipedia.
- `scraper/parser.py` : Parsing du HTML et extraction des informations clés.
- `scraper/saver.py` : Sauvegarde des fichiers HTML et JSON.
- `data/raw/` : Contient les fichiers HTML bruts.
- `data/processed/` : Contient les fichiers JSON structurés.

## Installation

1. Clonez le dépôt :
	```powershell
	git clone <url-du-repo>
	```
2. Installez les dépendances :
	```powershell
	pip install -r requirements.txt
	```

## Utilisation

Exemple pour scraper un article :

```python
from main import scrape_single_article
url = "https://fr.wikipedia.org/wiki/Python_(langage)"
article = scrape_single_article(url)
```

Les fichiers extraits seront sauvegardés dans le dossier `data`.

## Dépendances

- requests
- beautifulsoup4
- pandas
- numpy
- tqdm

## Auteur

Développé par Hassan Essoufi

## Licence

Ce projet est open-source et libre d'utilisation.

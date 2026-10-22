# Projet scraping

Petit programme Python qui récupère des produits sur un site, les enregistre dans une base SQLite, puis les exporte en CSV avec quelques statistiques.

## Comment ça marche

J'ai suivi le pipeline vu en cours : télécharger, analyser, extraire, enregistrer.

- Selenium ouvre Chrome (sans fenêtre si `HEADLESS = True`), charge la page avec le JavaScript et récupère le HTML.
- `parsing.py` cherche les cartes produit avec des sélecteurs CSS et crée des objets `Produit`.
- `depot.py` enregistre les produits dans `data/produits.db`. La colonne `url` est unique, donc relancer le scraping n'ajoute pas de doublons.
- `export_view.py` écrit un CSV séparé par `;` dans `exports/`, et calcule le prix moyen, le prix maximum et le nombre de produits par catégorie.
- `scraping_controller.py` parcourt les catégories de `config.py`, enregistre les produits et lance l'export.
- `main.py` affiche un menu dans la console.

Il y a des pauses aléatoires entre les requêtes pour ne pas surcharger le site. Si un CAPTCHA apparaît, le scraper s'arrête et garde les produits déjà récupérés.

## Installation

Dans le dossier du projet :

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Chrome doit être installé sur la machine.

## Utilisation

```bash
python main.py
```

Dans le menu :

1. Lancer le scraping.
2. Afficher les produits et les statistiques, puis exporter le CSV.
3. Quitter.

## Configuration

Les réglages sont dans `config.py` :

| Paramètre                            | Rôle                                                           |
| ------------------------------------ | -------------------------------------------------------------- |
| `AMAZON_URL`                         | Adresse du site                                                |
| `CATEGORIES`                         | Catégories à parcourir                                         |
| `PAGES_MAX`                          | Nombre de pages par catégorie (1 pour tester, 3 pour le rendu) |
| `HEADLESS`                           | `True` pour lancer Chrome sans fenêtre                         |
| `DELAI_ENTRE_PAGES`, `DELAI_LECTURE` | Pauses aléatoires, en secondes                                 |
| `USER_AGENT`                         | Identification du programme                                    |

## Structure

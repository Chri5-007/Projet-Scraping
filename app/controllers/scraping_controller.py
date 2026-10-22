from config import CATEGORIES, DB_PATH
from app.models.depot import Depot
from app.scraper.amazon_scraper import AmazonScraper
from app.views.export_view import exporter_csv, statistiques


class ScrapingController:
    def __init__(self, chemin_db=DB_PATH):
        self.depot = Depot(chemin_db)

    def lancer(self, categories=CATEGORIES):
        for categorie in categories:
            print(f"Scraping : {categorie}")
            produits = AmazonScraper().scraper(categorie)
            for p in produits:
                self.depot.ajouter(p)
            print(f"  {len(produits)} produits récupérés")

    def exporter(self):
        produits = self.depot.tous()
        chemin = exporter_csv(produits)
        print(f"CSV créé : {chemin}")
        for cle, valeur in statistiques(produits).items():
            print(f"{cle} : {valeur}")

    def fermer(self):
        self.depot.fermer()
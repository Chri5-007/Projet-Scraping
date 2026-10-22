from app.controllers.scraping_controller import ScrapingController
from app.views.console_view import (
    afficher_menu,
    afficher_produits,
    afficher_statistiques,
    afficher_succes,
    afficher_erreur,
)
from app.views.export_view import exporter_csv, statistiques


def main():
    controleur = ScrapingController()
    try:
        while True:
            choix = afficher_menu()
            if choix == "1":
                controleur.lancer()
                afficher_succes("Scraping terminé.")
            elif choix == "2":
                produits = controleur.depot.tous()
                afficher_produits(produits)
                afficher_statistiques(statistiques(produits))
                chemin = exporter_csv(produits)
                afficher_succes(f"CSV créé : {chemin}")
            elif choix == "3":
                break
            else:
                afficher_erreur("Choix invalide.")
    finally:
        controleur.fermer()


if __name__ == "__main__":
    main()
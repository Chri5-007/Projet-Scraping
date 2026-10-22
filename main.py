from app.controllers.scraping_controller import ScrapingController
from app.views.console_view import afficher_produits, afficher_statistiques
from app.views.export_view import statistiques


def menu():
    print("\n1. Lancer le scraping")
    print("2. Exporter le CSV et afficher les statistiques")
    print("3. Quitter")
    return input("Choix : ").strip()


def main():
    controleur = ScrapingController()
    try:
        while True:
            choix = menu()
            if choix == "1":
                controleur.lancer()
            elif choix == "2":
                produits = controleur.depot.tous()
                afficher_produits(produits)
                afficher_statistiques(statistiques(produits))
                controleur.exporter()
            elif choix == "3":
                break
            else:
                print("Choix invalide.")
    finally:
        controleur.fermer()


if __name__ == "__main__":
    main()
    
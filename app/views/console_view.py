from colorama import Fore, Style, init

init(autoreset=True)

LARGEUR = 46

ICONES = {
    "scraping": "🔍",
    "export": "📦",
    "quitter": "🚪",
    "succes": "✔",
    "erreur": "✖",
    "stats": "📊",
}


def afficher_titre():
    print(Fore.CYAN + Style.BRIGHT + "=" * LARGEUR)
    print("  SCRAPING DE PRODUITS".center(LARGEUR))
    print("=" * LARGEUR + Style.RESET_ALL)


def afficher_menu():
    afficher_titre()
    options = [
        ("1", ICONES["scraping"], "Lancer le scraping"),
        ("2", ICONES["export"], "Afficher et exporter les produits"),
        ("3", ICONES["quitter"], "Quitter"),
    ]
    for numero, icone, texte in options:
        print(f"  {Fore.YELLOW}{Style.BRIGHT}[{numero}]{Style.RESET_ALL} {icone}  {texte}")
    print(Fore.CYAN + "-" * LARGEUR + Style.RESET_ALL)
    return input(f"{Fore.GREEN}Ton choix : {Style.RESET_ALL}").strip()


def afficher_succes(message):
    print(Fore.GREEN + Style.BRIGHT + f"{ICONES['succes']} " + message + Style.RESET_ALL)


def afficher_erreur(message):
    print(Fore.RED + Style.BRIGHT + f"{ICONES['erreur']} " + message + Style.RESET_ALL)


def afficher_statistiques_titre():
    print(Fore.CYAN + Style.BRIGHT + f"\n{ICONES['stats']} Statistiques" + Style.RESET_ALL)










def afficher_produits(produits, limite=5):
    print(f"\n{len(produits)} produits enregistrés")
    for p in produits[:limite]:
        prix = f"{p.prix:.2f}" if p.prix is not None else "prix inconnu"
        print(f"- {p.titre[:60]} | {prix} | {p.categorie}")


def afficher_statistiques(stats):
    print("\nStatistiques")
    moyenne = stats["moyenne"]
    maximum = stats["maximum"]
    print(f"Prix moyen : {moyenne:.2f}" if moyenne is not None else "Prix moyen : aucune donnée")
    print(f"Prix maximum : {maximum:.2f}" if maximum is not None else "Prix maximum : aucune donnée")
    print("Nombre de produits par catégorie :")
    for categorie, nombre in stats["par_categorie"].items():
        print(f"  {categorie} : {nombre}")
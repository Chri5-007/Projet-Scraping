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
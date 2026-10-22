import csv
from pathlib import Path

from config import EXPORT_DIR

def exporter_csv(produits, nom="produits.csv", dossier=EXPORT_DIR):
    dossier = Path(dossier)
    dossier.mkdir(parents=True, exist_ok=True)
    chemin = dossier / nom
    produits_tries = sorted(
        produits,
        key=lambda p: (p.categorie or "", p.prix if p.prix is not None else float("inf")),
    )
    with open(chemin, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["categorie", "prix", "titre", "url", "image_url"])
        for p in produits_tries:
            writer.writerow([
                p.categorie,
                f"{p.prix:.2f}".replace(".", ",") if p.prix is not None else "",
                p.titre,
                p.url,
                p.image_url,
            ])
    return chemin


def statistiques(produits):
    prix = [p.prix for p in produits if p.prix is not None]
    moyenne = sum(prix) / len(prix) if prix else None
    maximum = max(prix) if prix else None
    par_categorie = {}
    for p in produits:
        par_categorie[p.categorie] = par_categorie.get(p.categorie, 0) + 1
    return {"moyenne": moyenne, "maximum": maximum, "par_categorie": par_categorie}
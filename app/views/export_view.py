import csv
from pathlib import Path

from config import EXPORT_DIR


def exporter_csv(produits, nom="produits.csv", dossier=EXPORT_DIR):
    dossier = Path(dossier)
    dossier.mkdir(parents=True, exist_ok=True)
    chemin = dossier / nom
    with open(chemin, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["titre", "prix", "image_url", "url", "categorie"])
        for p in produits:
            writer.writerow([p.titre, p.prix, p.image_url, p.url, p.categorie])
    return chemin


def statistiques(produits):
    prix = [p.prix for p in produits if p.prix is not None]
    moyenne = sum(prix) / len(prix) if prix else None
    maximum = max(prix) if prix else None
    par_categorie = {}
    for p in produits:
        par_categorie[p.categorie] = par_categorie.get(p.categorie, 0) + 1
    return {"moyenne": moyenne, "maximum": maximum, "par_categorie": par_categorie}
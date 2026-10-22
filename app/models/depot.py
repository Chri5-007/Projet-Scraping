import sqlite3
from pathlib import Path

from app.models.produit import Produit


class Depot:
    def __init__(self, chemin):
        if str(chemin) != ":memory:":
            Path(chemin).parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(chemin))
        self.conn.execute(
            """CREATE TABLE IF NOT EXISTS produits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titre TEXT,
                prix REAL,
                image_url TEXT,
                url TEXT UNIQUE,
                categorie TEXT
            )"""
        )
        self.conn.commit()

    def ajouter(self, p):
        self.conn.execute(
            "INSERT OR IGNORE INTO produits (titre, prix, image_url, url, categorie) "
            "VALUES (?, ?, ?, ?, ?)",
            (p.titre, p.prix, p.image_url, p.url, p.categorie),
        )
        self.conn.commit()

    def tous(self):
        lignes = self.conn.execute(
            "SELECT titre, prix, image_url, url, categorie FROM produits"
        ).fetchall()
        return [Produit(*ligne) for ligne in lignes]

    def fermer(self):
        self.conn.close()
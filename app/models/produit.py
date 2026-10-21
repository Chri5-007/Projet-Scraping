from dataclasses import dataclass


@dataclass
class Produit:
    titre: str
    prix: float | None
    image_url: str
    url: str
    categorie: str = ""
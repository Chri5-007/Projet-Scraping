import re

from selenium.webdriver.common.by import By

from app.models.produit import Produit

SEL_CARTE = "div[data-component-type='s-search-result']"
SEL_TITRE = "h2 span"
SEL_LIEN = "h2 a"
SEL_PRIX = "span.a-price span.a-offscreen"
SEL_IMAGE = "img.s-image"


def convertir_prix(texte):
    """'XOF 15,154' -> 15154.0 ; '29,99 €' -> 29.99 ; '1 299,99 €' -> 1299.99 ; '1,299.99' -> 1299.99 ; '' -> None"""
    nombre = re.sub(r"[^\d.,]", "", texte)
    if not nombre:
        return None
    decimales = re.search(r"[.,](\d{1,2})$", nombre)
    if decimales:
        entier = re.sub(r"[.,]", "", nombre[:decimales.start()])
        return float(f"{entier}.{decimales.group(1)}")
    return float(re.sub(r"[.,]", "", nombre))


def _premier(carte, selecteur):
    trouves = carte.find_elements(By.CSS_SELECTOR, selecteur)
    return trouves[0] if trouves else None


def _texte(element):
    return (element.get_attribute("textContent") or "").strip() if element else ""


def extraire_produits(driver, categorie=""):
    produits = []
    for carte in driver.find_elements(By.CSS_SELECTOR, SEL_CARTE):
        if not carte.get_attribute("data-asin"):
            continue
        titre = _texte(_premier(carte, SEL_TITRE))
        lien = _premier(carte, SEL_LIEN)
        if not titre or not lien or not lien.get_attribute("href"):
            continue
        image = _premier(carte, SEL_IMAGE)
        produits.append(
            Produit(
                titre=titre,
                prix=convertir_prix(_texte(_premier(carte, SEL_PRIX))),
                image_url=image.get_attribute("src") if image else "",
                url=lien.get_attribute("href"),
                categorie=categorie,
            )
        )
    return produits
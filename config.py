from pathlib import Path
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

AMAZON_URL = "https://www.amazon.fr"
DEPARTEMENT = "electronics"   # rayon High-Tech d'Amazon.fr
CATEGORIES = ["smartphone", "ordinateur portable", "casque audio"]
HEADLESS = True
PAGES_MAX = 1
DELAI_ENTRE_PAGES = (3, 6)  
DELAI_LECTURE = (1.5, 4)    
TIMEOUT = 15
USER_AGENT = "ProjetScrapingIIT/1.0 (projet etudiant)"

DB_PATH = BASE_DIR / "data" / "produits.db"
EXPORT_DIR = BASE_DIR / "exports"
TELECHARGER_IMAGES = True
IMAGES_DIR = BASE_DIR / "data" / "images"
def pause(plage):
    return random.uniform(*plage)
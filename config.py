from pathlib import Path
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

AMAZON_URL = "https://www.amazon.fr"
HEADLESS = True
PAGES_MAX = 3
DELAI_ENTRE_PAGES = (3, 6)   # pause avant la page suivante (s)
DELAI_LECTURE = (1.5, 4)     # temps passé sur une page avant analyse (s)
TIMEOUT = 15
USER_AGENT = "ProjetScrapingIIT/1.0 (projet etudiant)"

DB_PATH = BASE_DIR / "data" / "produits.db"
EXPORT_DIR = BASE_DIR / "exports"
TELECHARGER_IMAGES = True
IMAGES_DIR = BASE_DIR / "data" / "images"
def pause(plage):
    """Durée aléatoire (décimale) dans la plage (min, max)."""
    return random.uniform(*plage)
import hashlib
from pathlib import Path
from urllib.request import urlopen


def telecharger_image(url, dossier, ouvrir=urlopen):
    if not url:
        return ""
    dossier = Path(dossier)
    dossier.mkdir(parents=True, exist_ok=True)
    chemin = dossier / (hashlib.md5(url.encode()).hexdigest()[:12] + ".jpg")
    try:
        with ouvrir(url, timeout=15) as reponse:
            chemin.write_bytes(reponse.read())
    except Exception:
        return ""
    return str(chemin)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import HEADLESS, USER_AGENT


def creer_driver():
    options = Options()
    if HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--lang=fr-FR")
    options.add_argument(f"--user-agent={USER_AGENT}")
    return webdriver.Chrome(options=options)
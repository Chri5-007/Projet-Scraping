import time
from urllib.parse import quote_plus

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from app.scraper.driver import creer_driver
from app.scraper.parsing import SEL_CARTE, extraire_produits
from config import (AMAZON_URL, DELAI_ENTRE_PAGES, DELAI_LECTURE,
                    DEPARTEMENT, PAGES_MAX, TIMEOUT, pause)


class CaptchaDetecte(Exception):
    pass


class AmazonScraper:
    def scraper(self, recherche):
        driver = creer_driver()
        produits = []
        try:
            for page in range(1, PAGES_MAX + 1):
                url = f"{AMAZON_URL}/s?k={quote_plus(recherche)}&i={DEPARTEMENT}&page={page}"
                print(f"[{recherche}] page {page}/{PAGES_MAX}...")
                driver.get(url)
                self._verifier_captcha(driver)
                try:
                    WebDriverWait(driver, TIMEOUT).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, SEL_CARTE))
                    )
                except TimeoutException:
                    print("Aucun résultat sur cette page, arrêt.")
                    break
                time.sleep(pause(DELAI_LECTURE))
                produits += extraire_produits(driver, recherche)
                if page < PAGES_MAX:
                    time.sleep(pause(DELAI_ENTRE_PAGES))
        except CaptchaDetecte:
            print("CAPTCHA détecté : arrêt, produits déjà récupérés conservés.")
        finally:
            driver.quit()
        return produits

    @staticmethod
    def _verifier_captcha(driver):
        if driver.find_elements(By.CSS_SELECTOR, "form[action*='validateCaptcha']"):
            raise CaptchaDetecte()
"""
    Module for scraping Google Shopping.
"""

import logging
import random
import time

from typing import List

from pydantic import ValidationError
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementClickInterceptedException,
    ElementNotInteractableException,
    StaleElementReferenceException,
)
from webdriver_manager.chrome import ChromeDriverManager

from google_shopping_scraper.conf import google_shopping_scraper_settings
from google_shopping_scraper.models import ShoppingItem


logging.getLogger("WDM").setLevel(logging.ERROR)


class ConsentFormAcceptError(BaseException):
    message = "Unable to accept Google consent form."


class DriverInitializationError(BaseException):
    message = "Unable to initialize Chrome webdriver for scraping."


class DriverGetShoppingDataError(BaseException):
    message = "Unable to get Google Shopping data with Chrome webdriver."

class DriverScrollAndLoadAllError(BaseException):
    message = "Unable to scroll and load all items with Chrome webdriver."


class GoogleShoppingScraper:
    """Class for scraping Google Shopping"""

    def __init__(self, logger: logging.Logger | None = None) -> None:
        self._logger = logger if logger else logging.getLogger(__name__)
        self._consent_button_id = "L2AGLb"

    def _init_chrome_driver(self) -> webdriver.Chrome:
        """Initializes Chrome webdriver with full user agent spoofing"""
        
        profiles = [
            # Windows Chrome 142
            {
                "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
                "platform": "Windows",
                "platformVersion": "10.0.0",
                "architecture": "x86",
                "bitness": "64",
                "mobile": False,
                "model": "",
                "wow64": False,
                "brands": [
                    {"brand": "Chromium", "version": "142"},
                    {"brand": "Google Chrome", "version": "142"},
                    {"brand": "Not_A Brand", "version": "99"},
                ],
                "fullVersionList": [
                    {"brand": "Chromium", "version": "142.0.7444.60"},
                    {"brand": "Google Chrome", "version": "142.0.7444.60"},
                    {"brand": "Not_A Brand", "version": "99.0.0.0"},
                ],
            },
            # Windows Chrome 141
            {
                "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
                "platform": "Windows",
                "platformVersion": "10.0.0",
                "architecture": "x86",
                "bitness": "64",
                "mobile": False,
                "model": "",
                "wow64": False,
                "brands": [
                    {"brand": "Chromium", "version": "141"},
                    {"brand": "Google Chrome", "version": "141"},
                    {"brand": "Not_A Brand", "version": "99"},
                ],
                "fullVersionList": [
                    {"brand": "Chromium", "version": "141.0.7390.125"},
                    {"brand": "Google Chrome", "version": "141.0.7390.125"},
                    {"brand": "Not_A Brand", "version": "99.0.0.0"},
                ],
            },
            # macOS Chrome 142
            {
                "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
                "platform": "macOS",
                "platformVersion": "15.6.1",
                "architecture": "arm",
                "bitness": "64",
                "mobile": False,
                "brands": [
                    {"brand": "Chromium", "version": "142"},
                    {"brand": "Google Chrome", "version": "142"},
                    {"brand": "Not_A Brand", "version": "99"},
                ],
                "fullVersionList": [
                    {"brand": "Chromium", "version": "142.0.7444.60"},
                    {"brand": "Google Chrome", "version": "142.0.7444.60"},
                    {"brand": "Not_A Brand", "version": "99.0.0.0"},
                ],
            },
            # macOS Chrome 141
            {
                "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
                "platform": "macOS",
                "platformVersion": "15.6.1",
                "architecture": "arm",
                "bitness": "64",
                "mobile": False,
                "brands": [
                    {"brand": "Chromium", "version": "141"},
                    {"brand": "Google Chrome", "version": "141"},
                    {"brand": "Not_A Brand", "version": "99"},
                ],
                "fullVersionList": [
                    {"brand": "Chromium", "version": "141.0.7390.123"},
                    {"brand": "Google Chrome", "version": "141.0.7390.123"},
                    {"brand": "Not_A Brand", "version": "99.0.0.0"},
                ],
            },
        ]
        
        selected = random.choice(profiles)
        
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        user_agent_metadata = {
            "brands": selected["brands"],
            "fullVersionList": selected["fullVersionList"],
            "platform": selected["platform"],
            "platformVersion": selected["platformVersion"],
            "architecture": selected["architecture"],
            "bitness": selected["bitness"],
            "mobile": selected["mobile"],
        }
        
        if selected["platform"] == "Windows":
            user_agent_metadata["wow64"] = selected.get("wow64", False)
            user_agent_metadata["model"] = selected.get("model", "")
        
        driver.execute_cdp_cmd("Network.setUserAgentOverride", {
            "userAgent": selected["ua"],
            "platform": selected["platform"],
            "userAgentMetadata": user_agent_metadata
        })
        
        return driver

    def _click_consent_button(self, driver: webdriver.Chrome, query: str) -> None:
        """Clicks google consent form with selenium Chrome webdriver"""
        self._logger.info("Accepting consent form..")
        url = google_shopping_scraper_settings.get_shopping_url(query)
        try:
            driver.get(url)
            consent_button = driver.find_element(
                By.ID,
                self._consent_button_id,
            )
            consent_button.click()
            time.sleep(2)

        except NoSuchElementException:
            self._logger.warning("Consent form button not found.")
        except Exception as e:
            raise ConsentFormAcceptError from e

    def _scroll_and_load_all(self, driver: webdriver.Chrome, max_iterations: int = 50) -> None:
        """Scrolls and loads content without any JS viewport checks."""
        
        MORE_BUTTON = '[aria-label="More results"][style="transform: scale(1);"]'
        FOOTER = "#footcnt"
        
        iterations = 0
        
        while iterations < max_iterations:
            iterations += 1
            
            if self._is_at_end(driver, FOOTER, MORE_BUTTON):
                self._logger.info("Reached the end.")
                break
            
            button = self._find_element(driver, MORE_BUTTON)
            
            if button:
                if self._try_click(driver, button):
                    self._logger.info("Clicked 'More results'")
                    time.sleep(random.uniform(1.5, 3.0))
                    continue
            
            scroll_amount = random.randint(300, 700)
            ActionChains(driver).scroll_by_amount(0, scroll_amount).perform()
            time.sleep(random.uniform(0.3, 1.1))
        
        self._logger.info(f"Finished after {iterations} iterations.")

    def _try_click(self, driver: webdriver.Chrome, element) -> bool:
        """Attempt to click, return True if successful."""
        try:
            ActionChains(driver).scroll_to_element(element).perform()
            time.sleep(random.uniform(0.2, 0.5))
            element.click()
            return True
        except (ElementClickInterceptedException, ElementNotInteractableException):
            return False
        except StaleElementReferenceException:
            return False

    def _find_element(self, driver: webdriver.Chrome, selector: str):
        """Returns element or None if not found."""
        try:
            return driver.find_element(By.CSS_SELECTOR, selector)
        except NoSuchElementException:
            return None

    def _is_at_end(self, driver: webdriver.Chrome, footer_selector: str, button_selector: str) -> bool:
        """Check if we're done — footer exists and is displayed, no button."""
        footer = self._find_element(driver, footer_selector)
        button = self._find_element(driver, button_selector)
        
        if footer and footer.is_displayed() and not button:
            return True
        return False

    def _get_data_from_item_div(self, div: webdriver.Chrome) -> ShoppingItem:
        """Retrieves shopping item data from a div element and returns it as a ShoppingItem object."""
        try:
            price = div.find_element(By.CLASS_NAME, "lmQWe").text
        except NoSuchElementException:
            price = None

        try:
            title = div.find_element(By.CLASS_NAME, "gkQHve").text
        except NoSuchElementException:
            title = None

        try:
            rating = div.find_element(By.CLASS_NAME, "yi40Hd").text
        except NoSuchElementException:
            rating = None
        
        try:
            reviews = div.find_element(By.CLASS_NAME, "RDApEe").text
        except NoSuchElementException:
            reviews = None

        try:
            store = div.find_element(By.CLASS_NAME, "WJMUdc").text
        except NoSuchElementException:
            store = None

        return ShoppingItem(
            price=price,
            title=title,
            rating=rating,
            reviews=reviews,
            store=store,
        )

    def _get_items_for_query(self, driver: webdriver.Chrome) -> List[ShoppingItem]:
        """Retrieves shopping item data from a Google Shopping page."""
        self._logger.info("Scraping Google shopping page..")
        time.sleep(5)

        items = driver.find_elements(By.CSS_SELECTOR, '[data-attrid="apg-product-result"] > .jXGmLc')

        item_data = []
        for div in items:
            try:
                item = self._get_data_from_item_div(div)
            except ValidationError:
                self._logger.error("Data missing from shopping item div. Skipping..")
                continue

            item_data.append(item)

        return item_data

    def get_shopping_data_for_query(self, query: str) -> List[ShoppingItem]:
        """
        Retrieves a list of shopping items in Google Shopping for a query.

        Returns:
            List[ShoppingItem]: A list of ShoppingItem objects.
        Raises:
            ConsentFormAcceptError: If the Google consent form cannot be accepted.
            DriverInitializationError: If the Chrome webdriver cannot be initialized.
            DriverGetShoppingDataError: If the shopping data cannot be scraped from the Google Shopping site.
        """
        self._logger.info(f"Retrieving shopping items for query {query}..")
        
        try:
            driver = self._init_chrome_driver()
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        except Exception as e:
            raise DriverInitializationError from e

        try:
            self._click_consent_button(driver, query)
            try:
                self._scroll_and_load_all(driver)
            except Exception as e:
                self._logger.warning(f"Scrolling failed, continuing with visible items: {e}")
            
            return self._get_items_for_query(driver)
        except ConsentFormAcceptError:
            raise
        except Exception as e:
            raise DriverGetShoppingDataError from e
        finally:
            driver.close()

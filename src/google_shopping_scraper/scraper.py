"""
    Module for scraping Google Shopping.
"""

import logging
import time

from typing import List

from pydantic import ValidationError
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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


class GoogleShoppingScraper:
    """Class for scraping Google Shopping"""

    def __init__(self, logger: logging.Logger | None = None) -> None:
        self._logger = logger if logger else logging.getLogger(__name__)
        self._consent_button_xpath = "/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button/span"

    def _init_chrome_driver(self) -> webdriver.Chrome:
        """Initializes Chrome webdriver"""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=chrome_options)

    def _click_consent_button(self, driver: webdriver.Chrome, query: str) -> None:
        """Clicks google consent form with selenium Chrome webdriver"""
        self._logger.info("Accepting consent form..")
        url = google_shopping_scraper_settings.get_shopping_url(query)
        try:
            driver.get(url)
            consent_button = driver.find_element(
                By.XPATH,
                self._consent_button_xpath,
            )
            consent_button.click()
        except NoSuchElementException:
            self._logger.warning("Consent form button not found.")
        except Exception as e:
            raise ConsentFormAcceptError from e

        time.sleep(2)

    def _get_data_from_item_div(self, div: webdriver.Chrome) -> ShoppingItem:
        """Retrieves shopping item data from a div element and returns it as a ShoppingItem object."""
        price = (
            div.find_element(
                By.CLASS_NAME,
                "XrAfOe",
            )
            .find_element(By.CLASS_NAME, "QIrs8")
            .text
        )
        delivery_price = div.find_element(By.CLASS_NAME, "vEjMR").text
        title = div.find_element(By.CLASS_NAME, "tAxDx").text

        try:
            review = (
                div.find_element(
                    By.CLASS_NAME,
                    "NzUzee",
                )
                .find_element(By.CLASS_NAME, "QIrs8")
                .text
            )
        except NoSuchElementException:
            review = None

        url = div.find_element(By.CLASS_NAME, "Lq5OHe").get_attribute("href")
        return ShoppingItem(
            price=price,
            delivery_price=delivery_price,
            title=title,
            review=review,
            url=url,
        )

    def _get_items_for_query(self, driver: webdriver.Chrome) -> List[ShoppingItem]:
        """Retrieves shopping item data from a Google Shopping page."""
        self._logger.info("Scraping Google shopping page..")
        time.sleep(5)

        items = driver.find_elements(By.CLASS_NAME, "i0X6df")

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
        except Exception as e:
            raise DriverInitializationError from e

        try:
            self._click_consent_button(driver, query)
        except Exception as e:
            driver.close()
            raise e

        try:
            return self._get_items_for_query(driver)
        except Exception as e:
            raise DriverGetShoppingDataError from e
        finally:
            driver.close()

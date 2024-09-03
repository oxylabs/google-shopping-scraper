"""
    Main module for collecting Google shopping data.
"""

import logging

from typing import List

import pandas as pd

from google_shopping_scraper.models import ShoppingItem
from google_shopping_scraper.scraper import GoogleShoppingScraper


DEFAULT_OUTPUT_FILE = "shopping.csv"


class GoogleShoppingDataCollector:
    """Data collector class for Google Shopping"""

    def __init__(
        self,
        output_file: str | None = None,
        logger: logging.Logger | None = None,
    ) -> None:
        self._scraper = GoogleShoppingScraper()
        self._output_file = output_file if output_file else DEFAULT_OUTPUT_FILE
        self._logger = logger if logger else logging.getLogger(__name__)

    def _save_to_csv(self, items: List[ShoppingItem]) -> None:
        """Saves given list of shopping items to a CSV file."""
        self._logger.info(f"Writing {len(items)} items to {self._output_file}..")
        shopping_items = [item.model_dump() for item in items]
        df = pd.DataFrame(shopping_items)
        df.to_csv(self._output_file)

    def save_shopping_data_for_query(self, query: str) -> None:
        """
        Scrapes data from Google Shopping for a given query string and stores it into a CSV file.

        Args:
            query (str): The query string for which to get shopping results.
        """
        self._logger.info(f"Getting Google Shopping data for query {query}..")
        try:
            items = self._scraper.get_shopping_data_for_query(query)
        except Exception:
            self._logger.exception(
                f"Error when scraping Google shopping for query {query}."
            )
            return

        if not items:
            self._logger.info("No items found for query.")
            return

        self._save_to_csv(items)

"""
    Config module for google_shopping_scraper.
"""

from urllib.parse import quote

from pydantic_settings import BaseSettings


class GoogleShoppingScraperSettings(BaseSettings):
    """Settings class for Google Shopping Scraper"""

    url: str = "https://www.google.com/search?tbm=shop"

    def get_shopping_url(self, query: str) -> str:
        """Returns a Google Shopping URL for a given query string."""
        encoded_query = quote(query)
        return f"{self.url}&q={encoded_query}"


google_shopping_scraper_settings = GoogleShoppingScraperSettings()

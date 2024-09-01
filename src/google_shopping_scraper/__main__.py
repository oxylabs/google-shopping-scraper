"""
    Main module for google_shopping_scraper.
"""

import logging

import click

from google_shopping_scraper.collector import GoogleShoppingDataCollector


logging.basicConfig(level=logging.INFO)


@click.command()
@click.option(
    "--query",
    help="The query for which to return Google Shopping results for.",
    required=True,
)
def scrape_google_shopping(query: str) -> None:
    collector = GoogleShoppingDataCollector()
    collector.save_shopping_data_for_query(query)


if __name__ == "__main__":
    scrape_google_shopping()

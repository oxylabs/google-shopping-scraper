"""
    Pydantic models for Google Shopping scraper.
"""

from pydantic import BaseModel


class ShoppingItem(BaseModel):
    title: str
    price: str
    delivery_price: str
    review: str | None
    url: str

"""
    Pydantic models for Google Shopping scraper.
"""

from pydantic import BaseModel


class ShoppingItem(BaseModel):
    title: str
    price: str
    rating: str | None 
    reviews: str | None
    store: str | None

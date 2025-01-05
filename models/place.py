#!/usr/bin/python3
""" Place Module for HBNB project """
from models import storage

class Place(BaseModel):
    """Representation of a Place."""

    # other attributes and methods...

    @property
    def reviews(self):
        """Returns a list of all reviews for the current place."""
        return storage.get_reviews_for_place(self.id)

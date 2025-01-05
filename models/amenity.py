#!/usr/bin/python3
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Amenity(BaseModel, Base):
    """Representation of an Amenity."""

    __tablename__ = 'amenities'  # Table name in the database

    name = Column(String(128), nullable=False)  # Column for the amenity name

    # Many-to-Many relationship between Amenity and Place through place_amenity
    place_amenities = relationship("Place",
                                   secondary="place_amenity",
                                   back_populates="amenities")


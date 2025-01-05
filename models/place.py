#!/usr/bin/python3
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

# Table to represent the Many-to-Many relationship
place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    """Representation of a Place."""

    __tablename__ = 'places'  # Table name in the database

    name = Column(String(128), nullable=False)  # Place name

    # Many-to-Many relationship between Place and Amenity
    amenities = relationship("Amenity",
                             secondary=place_amenity,
                             back_populates="place_amenities",
                             viewonly=False)

    # Other columns and relationships can be defined here


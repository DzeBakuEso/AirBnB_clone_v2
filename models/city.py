#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """Representation of a City."""

    __tablename__ = 'cities'
    
    name = Column(String(128), nullable=False)

    # Relationship with Place model
    places = relationship("Place", backref="city", cascade="all, delete-orphan")

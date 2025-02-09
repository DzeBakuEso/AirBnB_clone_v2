#!/usr/bin/python3
"""State Model"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
from models import storage
from os import getenv

class State(BaseModel, Base):
    """Representation of a State"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """Return list of City instances linked to the current State"""
            from models import storage
            return [city for city in storage.all(City).values() if city.state_id == self.id]

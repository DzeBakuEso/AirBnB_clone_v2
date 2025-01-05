#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City

class State(BaseModel, Base):
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state", cascade="all, delete")

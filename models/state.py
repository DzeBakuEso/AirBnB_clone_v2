#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel

class State(BaseModel):
    """ State class representing a state """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize a new state with attributes passed as kwargs """
        super().__init__(*args, **kwargs)
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

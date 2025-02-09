#!/usr/bin/python3
"""Database storage engine"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.state import State
from models.city import City
import os

class DBStorage:
    """Handles long term storage of data in a MySQL database"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database connection"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/{db}',
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query objects from the database"""
        if cls:
            return {f"{obj.__class__.__name__}.{obj.id}": obj
                    for obj in self.__session.query(cls).all()}
        else:
            objects = {}
            for model in [State, City]:  # Add other models if necessary
                for obj in self.__session.query(model).all():
                    objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
            return objects

    def new(self, obj):
        """Add a new object to the session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload the database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Close the current session"""
        self.__session.remove()

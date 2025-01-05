from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import Base

class DBStorage:
    __engine = None
    __session = None
    
    def __init__(self):
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{password}@{host}/{db}",
            pool_pre_ping=True
        )
        
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
        
        self.reload()

    def all(self, cls=None):
        """Retrieve all objects, or filter by class if provided."""
        from models import State, City  # Import locally to avoid circular import
        
        if cls is None:
            result = self.__session.query(State, City).all()
        else:
            result = self.__session.query(cls).all()
        
        return {f"{type(obj).__name__}.{obj.id}": obj for obj in result}

    def new(self, obj):
        """Add a new object to the session."""
        self.__session.add(obj)
    
    def save(self):
        """Commit the session to save changes."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the session."""
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        """Create all tables and initialize the session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

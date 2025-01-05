from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import Base  # Import BaseModel first, because it is not dependent on models

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage class and set up the connection to MySQL."""
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{password}@{host}/{db}",
            pool_pre_ping=True
        )

        # Drop all tables if the environment is "test"
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

        self.reload()

    def all(self, cls=None):
        """Retrieve all objects, or filter by class if provided."""
        # Import models locally to avoid circular import issues
        from models import State, City, User  

        if cls is None:
            # Query all States, Cities, and Users
            result = self.__session.query(State).all() + self.__session.query(City).all() + self.__session.query(User).all()
        else:
            # Query specific class (e.g., User, State, etc.)
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
        # Create all tables in the database
        Base.metadata.create_all(self.__engine)

        # Set up the session factory and initialize the session
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()


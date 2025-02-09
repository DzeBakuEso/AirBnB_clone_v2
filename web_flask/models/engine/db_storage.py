from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """Interacts with the MySQL database"""

    def close(self):
        """Call remove() method on the private session attribute"""
        self.__session.remove()

from models.city import City
import models

class State:
    """State class"""
    @property
    def cities(self):
        """Getter method that returns the list of City objects linked to the current State"""
        if models.storage_type != 'db':
            return [city for city in models.storage.all(City).values() if city.state_id == self.id]
        return []

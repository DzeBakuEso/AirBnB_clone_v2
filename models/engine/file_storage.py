import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """Serializes instances to a JSON file and deserializes back to instances."""

    __file_path = 'file.json'
    __objects = {}

    # Dictionary mapping class names to their respective class objects
    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }

    def all(self, cls=None):
        """Returns a dictionary of all objects currently in storage."""
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary."""
        if obj:
            self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """Saves the current state of the storage to the file."""
        try:
            with open(self.__file_path, 'w') as f:
                temp_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
                json.dump(temp_dict, f)

        except Exception as e:
            print(f"Error: Could not save data. {e}")

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    class_name = val.get('__class__', None)
                    if class_name and class_name in self.classes:
                        # Retrieve the actual class based on the class_name string
                        cls = self.classes[class_name]
                        # Correctly instantiate the class with the data
                        self.__objects[key] = cls(**val)
                    else:
                        print(f"Error: Class '{class_name}' not found in classes dictionary or is missing '__class__' field")
        except FileNotFoundError:
            print("Error: File not found. No objects loaded.")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in file. Could not reload data.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def delete(self, obj=None):
        """Deletes an object from storage dictionary."""
        if obj:
            key = f'{obj.__class__.__name__}.{obj.id}'
            if key in self.__objects:
                del self.__objects[key]
                self.save()
            else:
                print(f"Error: Object {obj} not found in storage.")

    # New method to retrieve all reviews for a place
    def get_reviews_for_place(self, place_id):
        """Returns a list of all reviews for the specified place."""
        all_reviews = self.all(Review)
        place_reviews = [review for review in all_reviews.values() if review.place_id == place_id]
        return place_reviews


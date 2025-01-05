import json

class FileStorage:
    """Handles the storage of all objects in a JSON file"""

    __objects = {}
    __file_path = 'file.json'

    def all(self, cls=None):
        """Returns a dictionary of all objects or objects of a specific class"""
        if cls is None:
            return FileStorage.__objects
        else:
            filtered_objects = {}
            for key, obj in FileStorage.__objects.items():
                if isinstance(obj, cls):
                    filtered_objects[key] = obj
            return filtered_objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        # Dictionary mapping class names to their respective class objects
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }

        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    class_name = val['__class__']
                    if class_name in classes:
                        # Get the actual class using the class name
                        cls = classes[class_name]
                        # Instantiate the object using the class and data from the JSON
                        self.all()[key] = cls(**val)
                    else:
                        print(f"Error: {class_name} not found in classes dictionary")
        except FileNotFoundError:
            print("Error: File not found. No objects loaded.")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in file. Could not reload data.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def delete(self, obj=None):
        """Deletes obj from __objects if it exists"""
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
                self.save()

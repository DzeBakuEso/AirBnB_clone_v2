#!/usr/bin/python3 
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place

class FileStorage:
    """Serializes instances to a JSON file and deserializes back to instances."""

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of all objects."""
        if cls:
            return {key: obj for key, obj in self.__objects.items() if isinstance(obj, cls)}
        return self.__objects

    def save(self):
        """Saves all objects to the JSON file."""
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Deserializes the JSON file to load all objects."""
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass

    def get_amenities_for_place(self, place_id):
        """Returns a list of Amenity instances linked to a specific Place."""
        # Get the place instance
        place = self.__objects.get(f"Place.{place_id}")
        if not place:
            return []

        # Get all amenities
        all_amenities = self.all(Amenity)

        # Find amenities linked to the place using its amenity_ids
        place_amenities = [amenity for amenity in all_amenities.values()
                           if amenity.id in getattr(place, 'amenity_ids', [])]
        return place_amenities

    def set_amenities_for_place(self, place, amenity):
        """Appends an Amenity.id to the place's amenity_ids."""
        if isinstance(amenity, Amenity):
            if place.id not in place.amenity_ids:
                place.amenity_ids.append(amenity.id)
                self.save()

    def add_object(self, obj):
        """Adds an object to the storage."""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj
            self.save()

    def delete(self, obj=None):
        """Deletes an object from the storage."""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    def get(self, cls, id):
        """Returns an object based on the class name and id."""
        return self.__objects.get(f"{cls.__name__}.{id}")


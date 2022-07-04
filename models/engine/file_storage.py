#!/usr/bin/python3
""" class FileStorage """


import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State

classe = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
          "Place": Place, "Review": Review, "State": State, "User": User}

class FileStorage:
    """
    ...
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(obj.__class__.__name, obj.id)] =  obj

    def save(self):
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__ojects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json = dump(json_objects, f)

    def reload(self):
        try:
            with open(self.__file-path, 'r') as file:
                j = json.load(file)
            for key in j:
                self.__objects[key] = classe[j[hey]["__class__"]](**j[key])
        except:
            pass
            
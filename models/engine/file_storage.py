"""
This is the "file_storage" module.
The file_storage module supplies one class, FileStorage, that\
that serializes instances to a JSON file and deserializes JSON\
file to instances.

For example,
FileStorage()
"""
import json


class FileStorage:
    """Defines a class FileStorage.

    Attributes:
        __file_path (str): id of the class
        __objects (dictionary): created date of the class
    """

    __file_path = "storage.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return __objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_key = obj.__class__.__name__ + ".id"
        __objects.update({'obj_key': obj})

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(__file_path, 'w') as f:
            f.write(json.dumps(__objects))

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON\
        file (__file_path) exists.
        """
        with open(__file_path, "r") as f:
            __objects = json.loads(f.read())

#!/usr/bin/python3
"""
This is the "base_model" module.
The base_model module supplies one class, BaseModel, that
	defines all common attributes/methods for other classes.

For example,
BaseModel()
"""
import uuid
from datetime import date

class BaseModel:
    """Defines a class BaseModel.

    Attributes:
        id (str): id of the class 
        created_at (str): created date of the class
        updated_at (str): updated date of the class 
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = date.today()
        self.updated_at = self.created_at

    def __str__(self):
        """Unofficial string representation of BaseModel class."""
        return "[{}] ({:d}) {}".\
            format(self.__name__, self.id, self.__dict__)

    def save(self):
        """Defines a function save.

        Updates the public instance attribute updated_at with the
        current datetime.
        """
        self.updated_at = date.today()

    def to_dict(self):
        """Defines a function to_dict.

        Updates the public instance attribute updated_at with the
        current datetime.
        """
        dict_r = self.__dict__
        dict_r.update({'__class__': 'self.__name__'},
                      {'created_at': self.created_at.isoformat()},
                      {'updated_at': self.updated_at.isofromat()})
        return dict_r    

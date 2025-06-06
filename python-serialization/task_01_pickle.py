#!/usr/bin/env python3
"""
Module: task_01_pickle

This module defines a custom class `CustomObject` that demonstrates how to
serialize and deserialize Python objects using the `pickle` module.

Usage:
    - Create an instance of `CustomObject`
    - Call `serialize(filename)` to save it to a file
    - Call `CustomObject.deserialize(filename)` to load the object from a file
"""
import pickle


class CustomObject:
    """
    A class to represent a custom object with attributes and
    support for pickling (serialization/deserialization).

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Indicates whether the person is a student.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a new instance of CustomObject.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes of the object in a readable format.
        """
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Is Student : {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object and save it to a file.

        Args:
            filename (str): The name of the file to save the object in.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception as e:
            print(f"Error during serialization: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize and return a CustomObject instance from a file.

        Args:
            filename (str): The name of the file to load the object from.

        Returns:
            CustomObject: The deserialized object, or None if an error occurs.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception as e:
            print(f"Error during deserialization: {e}")
            return None

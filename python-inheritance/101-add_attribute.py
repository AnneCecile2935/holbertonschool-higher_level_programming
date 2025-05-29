#!/usr/bin/python3
"""
Module that defines a function to add a new attribute to an object if possible.

Raises:
    TypeError: If the object cannot have new attributes added.
"""


def add_attribute(object, attribute, value):
    """
    Adds a new attribute to the given object if it supports dynamic
     attribute assignment.

    Parameters:
        object (any): The object to which the attribute should be added.
        attribute (str): The name of the attribute to add.
        value (any): The value to assign to the new attribute.

    Raises:
        TypeError: If the object cannot have new attributes added (e.g.,
        built-in types like str).

    Explanation:
        - Checks if the object has a __dict__ attribute, which stores instance
         attributes.
        - If the object's class defines __slots__, checks if '__dict__'
        is among them.
          If not, dynamic attribute addition is not allowed.
        - If checks pass, uses setattr to add the attribute.
    """
    cls = object.__class__
    if not hasattr(object, '__dict__'):
        raise TypeError("can't add new attribute")

    if hasattr(cls, '__slots__'):
        slots = cls.__slots__
        if isinstance(slots, str):
            slots = (slots,)
        if '__dict__' not in slots:
            raise TypeError("can't add new attribute")
    setattr(object, attribute, value)

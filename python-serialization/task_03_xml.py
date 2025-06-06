#!/usr/bin/env python3
"""
Module: task_03_xml

This module provides functions for serializing and deserializing
Python dictionaries
to and from XML format using the built-in xml.etree.ElementTree module.

Functions:
- serialize_to_xml(dictionary, filename): Converts a Python dictionary
into an XML file.
- deserialize_from_xml(filename): Reads XML data from a file and converts
it back into a Python dictionary.

This is useful for scenarios where XML is preferred or required over formats
like JSON.
"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.

    Each key-value pair in the dictionary is converted to an XML element
    under a root element <data>.
    The resulting XML is written to the specified filename.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The path to the XML file to write.

    Returns:
        bool: True if serialization was successful, False otherwise.
    """
    try:
        root = ET.Element('data')
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="UTF8", xml_declaration=True)
        return True

    except Exception as e:
        print(f"Error during serialisation : {e}")
        return False


def deserialize_from_xml(filename):
    """
    Serializes a Python dictionary into an XML file.

    Each key-value pair in the dictionary is converted to an XML element under
    a root element <data>.
    The resulting XML is written to the specified filename.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The path to the XML file to write.

    Returns:
        bool: True if serialization was successful, False otherwise.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        data = {}
        for child in root:
            data[child.tag] = child.text
        return data
    except Exception as e:
        print(f"Error during deserialization : {e}")
        return None

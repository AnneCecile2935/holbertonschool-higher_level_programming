# Python - Classes and Objects

## Description

This project is focused on learning the basics of Object-Oriented Programming (OOP) in Python. It covers the creation of classes, defining attributes, using methods, and implementing encapsulation, data abstraction, and property setters/getters. Additionally, it explores how to handle private instance attributes and how to define and use custom classes to model real-world entities.

## Learning Objectives

- What is OOP and how is it implemented in Python

Object-Oriented Programming (OOP) is a way to structure code using "objects."
An object is like a box that holds data (called attributes) and actions
(called methods)

- The difference between a class and an object

A class is the general template, and the object is a concrete version
of that template. An object is created from a class.

- How to define and use attributes and methods

An attribute is a variable that belongs to a class or an object.
It is a characteristic or a property.

A method is a function defined inside a class.
It acts on the object's attributes.

- What is the difference between an attribute and a property?

Attribute: A directly accessible variable.
Property: A method that acts like a variable.

- The purpose of the `__init__` method

__init__ is a special method that is automatically called
when an object is created. It initializes the attributes.

- How to define and use property setters and getters

The Pythonic way is to use the @property decorator for the getter
and @attribute_name.setter for the setter.

- How to bind attributes to objects and classes?

You can directly assign a value to self.attribute_name for an object
or Class.attribute_name for a class.

- What is dict?

__dict__ is a dictionary that contains all the attributes of an object or class.

- What are public, protected, and private attributes?

Public: Accessible everywhere. Example: self.name
Protected: Prefixed with _, used only within the class and its subclasses.
Private: Prefixed with __, used only within the class.

- What is data abstraction, encapsulation, and information hiding?

Abstraction: Hiding complex details and showing only essential information.
Encapsulation: Grouping data and methods in a class.
Information hiding: Making certain information inaccessible from outside.

- How does Python find attributes?

Python first looks in the object, then in its class, and finally
in parent classes.

- How to use getattr()?

The getattr(obj, "attribute", default_value) function allows you
to access an object's attribute dynamically.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- Python version: 3.8.5
- All files should end with a new line
- Code must pass `pycodestyle` (version 2.7.*)
- All classes, methods, and functions must have a documentation string

## Project Structure

- **0-square.py** — An empty class `Square` that defines a square.
- **1-square.py** — A class `Square` with a private instance attribute `size`.
- **2-square.py** — A class `Square` with size validation.
- **3-square.py** — A class `Square` with a method to calculate the area.
- **4-square.py** — A class `Square` with getter and setter for `size`.
- **5-square.py** — A class `Square` with a method `my_print()` to print the square.
- **6-square.py** — A class `Square` with position validation and printing using space.

## Task Table

| Task | Description | File |
|------|-------------|------|
| 0    | Create an empty class `Square`. | 0-square.py |
| 1    | Define a class `Square` with a private attribute `size`. | 1-square.py |
| 2    | Add validation for `size` in the class `Square`. | 2-square.py |
| 3    | Implement a method `area()` to calculate the area of the square. | 3-square.py |
| 4    | Add getter and setter for `size` with validation. | 4-square.py |
| 5    | Implement the `my_print()` method to print the square using `#`. | 5-square.py |
| 6    | Add a `position` attribute to `Square` and print the square using space. | 6-square.py |

## Advanced Tasks

| Task | Description | File |
|------|-------------|------|
| 7    | Create a `Node` class for a singly linked list. | 100-singly_linked_list.py |
| 8    | Implement the `__str__` method to print the square instance. | 101-square.py |
| 9    | Add comparison methods to the `Square` class. | 102-square.py |

---

## Author

Anne-Cécicle Colléter


#!/usr/bin/python3
"""
Module: 100-singly_linked_list
Defines classes Node and SinglyLinkedList to represent
nodes and a singly linked list.
"""


class Node:
    """
    Represents a node in a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node or None): The next node in the list.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new Node object.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node or None): The next node in the list.

        Raises:
            TypeError: If data is not an integer.
            TypeError: If next_node is not a Node object or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data of the node.

        Args:
            value (int): The new data value.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the list.

        Args:
            value (Node or None): The next node.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if not (value is None or isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list of nodes.

    Methods:
        sorted_insert(value): Inserts a new node in a sorted position.
    """
    def __init__(self):
        """Initializes an empty singly linked list."""
        self.__head = None

    def __str__(self):
        """
        Returns a string representation of the list.

        The data of each node is printed on a separate line.
        """
        result = ""
        current = self.__head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.rstrip()

    def sorted_insert(self, value):
        """
        Inserts a new node into the list in sorted order.

        Args:
            value (int): The data value for the new node.
        """
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None
            and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

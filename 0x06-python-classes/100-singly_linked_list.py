#!/usr/bin/python3
"""Define Class Node."""

class Node:
    """Class Node representation."""

    def __init__(self, data, next_node=None):
        """Class Node intialization.

        Args:
            data (int): data
            next_node : node object
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)
    
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer.")
        self.__data = value

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

"""Define Class SinglyLinkedList."""

class SinglyLinkedList:
    """SinglyLinkedList representation."""

    def __init__(self):
        """Initialise, SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node in ordered numerical position to the SlinglyLinkedList.

        Args:
            value (Node): The new Node to insert.
        """

        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            current = self.__head
            while (current.next_node is not None and current.next_node.data < value):
                current = current.next_node
            new.next_node = current.next_node
            current.next_node = new

    def __str__(self):
        """Define the print representation."""
        val = []
        current = self.__head
        while current is not None:
            val.append(str(current.data))
            current = current.next_node
        return ('\n'.join(val))

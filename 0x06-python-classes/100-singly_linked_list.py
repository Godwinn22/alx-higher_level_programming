#!/usr/bin/python3
"""A class Node that defines a node of a singly linked list by"""


class Node:
    """
    Represents a node of a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node or None): Reference to the next
        node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a node with the given data and optional next node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): Reference to the
            next node (default is None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        int: Retrieves the data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data stored in the node.

        Args:
            value (int): The data to be stored in the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Node or None: Retrieves the reference to the next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the reference to the next node.

        Args:
            value (Node or None): Reference to
            the next node or None.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if value is not None or not isinstance(value, Node):
            raise TypeError("next_node must be a Node object or None")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.

    Attributes:
        head (Node or None): Reference to the
        first node in the linked list (default is None).
    """

    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.head = None

    def __str__(self):
        """
        Returns a string representation of the singly linked list.

        Returns:
            str: String representation of the linked list.
        """
        if self.head is None:
            return "Singly Linked List is empty"
        current = self.head
        linked_list_str = ""
        while current:
            linked_list_str += str(current.data) + "\n"
            current = current.next_node
        return linked_list_str

    def sorted_insert(self, value):
        """
        Inserts a new node with the given value into the
        correct sorted position in the linked list.

        Args:
            value (int): The value to be inserted into the linked list.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

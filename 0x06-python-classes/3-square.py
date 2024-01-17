#!/usr/bin/python3

# -*- coding: utf-8 -*-
""" A very simple module containing containing a simple class"""


class Square:
    """A Construct for Square objects
    """

    def __init__(self, size=0):
        """A method called everytime a new object is created

        Args:
            size: length/breadth of the square
        """

        self.size = size

    @property
    def size(self):
        """The getter method for the size attribute

        Note: The setter method ensures that it doesn't set
              the value of size, if it  lesser that 0, or it is not
              an integer.

        """

        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """A method to get the area of the square

        Return:
            The area of the square size * size

        """
        return self.__size ** 2

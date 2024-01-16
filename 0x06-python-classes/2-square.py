#!/usr/bin/python3

# -*- coding: utf-8 -*-
"""A module containing a square class"""


class Square:
    """A class that defines a squares

    Attributes:
        size: private instance for the squares magnitude

    """

    def __init__(self, size=0):
        """The object initialization method

        Args:
            size: The magnitude of the square that must be an integer

        """

        self.size = size

    @property
    def size(self):
        """The getter method to get the private instance

            The setter method raises a TypeError if any\
            while also ensuring size is an integer
        """
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

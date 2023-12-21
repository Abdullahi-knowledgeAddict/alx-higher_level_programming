#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Modules Documentation.

This module contains a class Square that defines by

    -> Private instance attribute: size
    -> Instantiation with size (no type/value verification)
"""


class Square:
    """A class that defines a Square with it size

    Attributes:
        Size: a prive instance variable
    """

    def __init__(self, size):
        """Initializing the instance

        args:
            Size: The initial size of the square
        """
        self.__size = size

        @property
        def size(self):
            """size: This is the setter property"""
            return size

        @size.setter
        def size(self, value):
            self.__size = value

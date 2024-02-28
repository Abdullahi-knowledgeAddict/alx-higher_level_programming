#!/usr/bin/python3

# -*- coding: utf-8 -*-
"""A module cotaining a single rectangle class
"""


class Rectangle:
    """A Rectangle class that defines a rectangle

    Attributes:
        print_symbol: Used as symbol for string representation
                      Initialized to '#'
        number_of_instances: keeping count of instances

    """

    # keeping count of instances
    number_of_instances = 0

    # Symbol for string representation
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes any new instance and increment
            the number_of_instances.

        Args:
            width: The width of rectangle, defaultely 0
            height: The width of rectangle, defaultely 0
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """The propert getter for width

        The setter raises TypeError or ValueError
        whenever the need arises
        """

        return self.__width

    @property
    def height(self):
        """The height getter property

        The height property setter raise TypeError or ValueError
        when necessary
        """

        return self.__height

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    # Extra methods
    def area(self):
        """Evaluates the Area of the rectangle

        Returns: The area of the rectangle object
        """

        return self.__height * self.__width

    def perimeter(self):
        """Evaluate the perimeter of the the rectangle

        Returns: The perimeter (Total length of the edges)
                But, zero (0)  is returned if either of the width of
                height are zero (0)
        """

        if self.__height == 0 or self.__width == 0:
            return 0

        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Generates the string representation of rectangle

        Return:
                A diagramatical representation of the rectangle
                defaultely  "#" for every unit and can be changed
                depending on the value of the 'print_symbol'
                (public attribute)
                if either of the dimension is zero
                an empty string is returned
        """

        if self.__width == 0 or self.__height == 0:
            return ""
        # Else the computated string is return
        # Slized to exclude last "\n" character
        return (((str(self.print_symbol) * self.__width) + "\n") *
                self.__height)[0:-1]

    def __repr__(self):
        """Generate a string representation of the object
            that can be reused by eval(), to regenerate the
            actual object.

            Return:
                    A string, that can be used to regenerate the objec
        """

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints \"Bye rectangle...\"
            whenever a rectangle object is
            deleted
        """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

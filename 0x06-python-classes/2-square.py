#!/usr/bin/python3
"""A class that defines a square"""


class Square:
    """A square class"""

    def __init__(self, size=0):
        """Square initialization

        Args:
            size (int)
        """
        if type(size) != int:
            raise TypeError("size must be an intenger")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

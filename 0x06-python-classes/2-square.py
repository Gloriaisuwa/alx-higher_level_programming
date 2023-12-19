#!/usr/bin/python3

"""A class square that defines a square based on 1-square.py"""


class Square:

    """
    Attributes:
        __size (int): Private instance attribute representing
        the size of the square.
    """

    def __init__(self, size=0):

         """
        Initializes a new instance of the Square class.

        Args:
            size (int): Size of the square. Default to 0.

        Raises:
             TypeError: If size is not an integer.
             ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

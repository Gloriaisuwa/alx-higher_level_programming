#!/usr/bin/python3

"""A class Square that defines a square based on 4-square.py"""

class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

            def area(self):
                return (self.__size ** 2)

            @property
            def size(self):
                return self.__size

            @size.setter
            def size(self, value):
                if not isinstance(value, int):
                    raise TypeError("size must be an integer")
                elif value < 0:
                    raise ValueError("size must be >= 0")
                else:
                    self.__size = value

    def my_print(self):
        print('\n'.join(['#' * self.__size for _ in range(self.__size)]) if
                self.__size else '')

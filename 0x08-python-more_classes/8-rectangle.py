#!/usr/bin/python3
"""Rectangle module
"""


class Rectangle:
    """Defines a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Args:
            width: width of a rectangle (int)
            height: height of a rectangle (int)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns:
            The width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets new value for width
        Raises:
            TypeError, ValueError
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns:
            The height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets new value for height
        Raises:
            TypeError, ValueError
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns:
            Area of a rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """Returns:
            Perimeter of a rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """Returns:
            String of a rectangle using #
        """
        if self.width == 0 or self.height == 0:
            return ("")
        row = ("{}".format(self.print_symbol)) * self.width
        pri = row
        for i in range(self.height - 1):
            pri += "\n" + row
        return pri

    def __repr__(self):
        """Returns:
            String representation of a rectangle
        """
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """Prints when an instance is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Args:
            rect_1: instance of rectangle to analyze
            rect_2: instance of rectangle to analyze
        Raises:
            TypeError
        Returns:
            rect_1 if both have the same area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

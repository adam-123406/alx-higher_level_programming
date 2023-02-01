#!/usr/bin/python3

"""
This is a module for a class Rectangle
"""


class Rectangle:
    """Class of that defines a rectangle by: (based on 1-rectangle.py)"""

    def __init__(self, width=0, height=0):
        """Initialize class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, widthValue):
        """Set width"""
        if type(widthValue) != int:
            raise TypeError("width must be an integer")
        if widthValue < 0:
            raise ValueError("width must be >= 0")
        self.__width = widthValue

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, HeightValue):
        """Set height"""
        if type(HeightValue) != int:
            raise TypeError("height must be an integer")
        if HeightValue < 0:
            raise ValueError("height must be >= 0")
        self.__height = HeightValue

    def area(self):
        """Calculate area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate perimeter"""
        width = self.__width
        height = self.__height
        if width == 0 or height == 0:
            return 0
        return (width + height) * 2
    
    
    
    
    
    
    
    
#!/usr/bin/python3

"""
This is a module for a class Rectangle
"""


class Rectangle:
"""Class of a Rectangle"""

def __init__(self, width=0, height=0):
"""Initialize class"""
self.width = width
self.height = height

@property
def width(self):
"""Get width"""
return self.__width

@width.setter
def width(self, widthValue):
"""Set width"""
if type(widthValue) != int:
raise TypeError("width must be an integer")
if widthValue < 0:
raise ValueError("width must be >= 0")
self.__width = widthValue

@property
def height(self):
"""Get height"""
return self.__height

@height.setter
def height(self, HeightValue):
"""Set height"""
if type(HeightValue) != int:
raise TypeError("height must be an integer")
if HeightValue < 0:
raise ValueError("height must be >= 0")
self.__height = HeightValue

def area(self):
"""Calculate area"""
return self.__width * self.__height

def perimeter(self):
"""Calculate perimeter"""
width = self.__width
height = self.__height
if width == 0 or height == 0:
return 0
return (width + height) * 2






#!/usr/bin/python3
""" empty class Rectangle that defines a rectangle
"""


class Rectangle:
""" class that defines a rectangle by: (based on 1-rectangle.py)"""
def __init__(self, width=0, height=0):
""" Instantiation with optional width and height"""
self.width = width
self.height = height

@property
def width(self):
""" width
"""
return self.__width

@property
def height(self):
""" height
"""
return self.__height

@width.setter
def width(self, value):
""" width setter
"""
if type(value) is not int:
raise TypeError("width must be an integer")
if value < 0:
raise ValueError("width must be >= 0")
self.__width = value

@height.setter
def height(self, value):
""" height setter
"""
if type(value) is not int:
raise TypeError("height must be an integer")
if value < 0:
raise ValueError("height must be >= 0")
self.__height = value

def area(self):
""" returns rectangle area"""
return self.__width * self.__height

def perimeter(self):
""" returns rectangle perimiter"""
if self.__width is 0 or self.__height is 0:
return 0
return self.__width * 2 + self.__height * 2
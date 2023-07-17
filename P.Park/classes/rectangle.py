class Rectangle:
    def __init__(self, width=1, height=1):
        self._width = width
        self._height = height

    def setWidth(self, width):
        self._width = width

    def getWidth(self):
        return self._width

    def setHeight(self, height):
        self._height = height

    def getHeight(self):
        return self._height

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def __str__(self):
        return ("Width: " + str(self._width) + "\nHeight: " + str(self._height)) 

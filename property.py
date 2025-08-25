class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    @width.setter
    def width(self, new_width):
        if new_width>0:
            self._width = new_width
        else:
            print("Width must be positive")

    @height.setter
    def height(self, new_height):
        if new_height>0:
            self._height = new_height
        else:
            print("height must be positive")

rect = Rectangle(10, 20)
rect.width = 30
rect.height = -5
print(rect.width)    
print(rect.height)
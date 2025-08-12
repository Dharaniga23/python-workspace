class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled
    
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color, is_filled)
        self.radius = radius

class Square(Shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self,color,is_filled,width,height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle(color  = "red", is_filled = True,radius = 5) 
square = Square(color = "yellow", is_filled = False, width = 7) 
triangle = Triangle(color = "green", is_filled = True, width = 4, height = 6)   

circle.describe()
print(circle.color)
print(square.width)
print(circle.is_filled)

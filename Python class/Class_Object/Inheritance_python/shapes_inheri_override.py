class Shape:  # Parent class

    def __init__(self, name):
        # Store the name of the shape in the object
        self.name = name

    def area(self):
        # Default area method for Shape (meant to be overridden)
        # If a child class does not override this, this message is printed
        print("Not implemented")

    def __str__(self):
        # User-friendly string when you do print(object)
        return "Shape named :" + self.name

    def __repr__(self):
        # Developer-friendly representation, used inside lists, etc.
        return self.name


class Rectangle(Shape):  # Rectangle inherits from Shape

    def __init__(self, name, width, height):
        # Call Shape's __init__ to set the name
        super().__init__(name)

        # Add rectangle-specific attributes
        self.width = width
        self.height = height

    def area(self):
        # Override area() to compute rectangle area
        print("Area of", self.name, self.width * self.height)


class Square(Rectangle):  # Square inherits from Rectangle (and indirectly from Shape)
    
    def __init__(self, name, width, height):
        # Reuse Rectangle's __init__ to set name, width, and height
        super().__init__(name, width, height)

class Circle(Shape):  # Circle inherits from Shape
    
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        # Circle area override: π * radius² (using 3.14159 for pi)
        area = 3.14159 * self.radius * self.radius
        print("Area of", self.name, area)


class Triangle(Shape):  # Triangle inherits from Shape
    
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height

    def area(self):
        # Triangle area override: (base * height) / 2
        area = (self.base * self.height) / 2
        print("Area of", self.name, area)




# Create a basic Shape object
shape = Shape("Basic Shape")
print(shape.name)   # prints: Basic Shape
shape.area()        # prints: Not implemented

# Create a Rectangle object
rect = Rectangle("Rectangle", 10, 5)
print(rect.name, rect.width, rect.height)  # prints: Rectangle 10 3
rect.area()                                # prints: Area of Rectangle 30

# Create a Square object
square = Square("Square", 6, 6)
square.area()  # prints: Area of Square 100

circle = Circle("Circle", 5)  #radius = 5
circle.area() # Area of Circle 78.53975

triangle = Triangle("Triangle", 10, 6)  #base = 10, height = 6
triangle.area()  # Area of Triangle 30.0

# Put all three objects into a list
# list = [square, rect, shape]

# # Printing each object uses __str__
# print(square)  # Shape named :Square
# print(rect)    # Shape named :Rectangle
# print(shape)   # Shape named :Basic Shape

# # Printing the list uses __repr__ for each element
# print(list)    # ['Square', 'Rectangle', 'Basic Shape']

# Test polymorphism with mixed list
shapes_list = [square, rect, shape, circle, triangle]
print("\nAll shapes in list:")
for s in shapes_list:
    s.area()

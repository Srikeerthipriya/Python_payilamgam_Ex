class Circle:

    def __init__(self,radius):
        self.radius = radius
        
    def area (self,shape):
        PI = 3.14
        area_circle = PI * self.radius**2
        print ("My surface area of",shape,"is",area_circle)

r = 9

circle = Circle(r)
circle.area("circle")
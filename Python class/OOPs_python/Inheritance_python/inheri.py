class Rectangle: # parent class 

    name = "rectangle"

    def __init__(self,width,height): # initiating the the fun wth parameter width & height 
        self.width = width
        self.height = height

    def area(self): # method for area 
        print("Area of ",self.name,self.width*self.height)

class Square(Rectangle): #  child class (inherits from rectangle)

    name = "square"

    def __init__(self, size): # initiation it will return the parent class parameter & extra parameter we have added size 
        super().__init__(size, size) # call Rectangle.__init__ with size for both width and height # fun super it will get the fun in parent class & then initate with new parameter size two times because of the 2 parameter in parent class 


rec = Rectangle(9,6)
rec.area()

sq = Square(5) 
sq.area()


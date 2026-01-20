class Sq:

    shape = "Square"

    def __init__(self,size):
        self.size = size 

    def area (self):
        area_sq = self.size * self.size
        print("My surface area of",self.shape,"is",area_sq)

size = 4
# shape = "square"
square = Sq(size)
square.shape = "Shape" # it will reflect in this particular area 
square.area()
        
square = Sq(5)
square.area()
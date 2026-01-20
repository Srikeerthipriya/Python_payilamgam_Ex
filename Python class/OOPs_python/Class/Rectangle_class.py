class Rec:

    def __init__(self,width,length):
        self.width = width
        self.length = length
        

    def area(self,shape):
        area_rec= self.width * self.length
        print("My surface area",shape,"is",area_rec)

        # area_sq = self.width * self.width
        # print("My surface area",shape,area_sq)  



wid = 5
len = 10
rectangle = Rec(wid,len)
rectangle.area("rectangle")


# square = Shapes(wid,len)
# square.area("square")
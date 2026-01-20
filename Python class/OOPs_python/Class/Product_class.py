class Product:
    
    def __init__(self,qty,price,sold):
        self.qty= qty
        self.price= price
        self.sold= sold

    def sell(self,sell_units):
        self.qty = self.qty - sell_units
        self.sold = self.sold + sell_units
        print("No of remaining qty :",self.qty)
        print("No of units sold:",self.sold)
        

    def buy(self,buy_units):
        self.qty = self.qty + buy_units
        print("total no of qty:",self.qty)
        print("no of units buy:",buy_units)

    def revenue(self):
        print("Revenue of product:",self.sold * self.price)



pen = Product(100,10,0)
pen.sell(20)
pen.buy(70)
pen.revenue()

pencil = Product(200,2,0)
pencil.sell(10)
pencil.buy(30)
pencil.revenue()


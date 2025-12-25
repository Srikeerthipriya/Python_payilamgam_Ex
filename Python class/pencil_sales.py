quantity = 100
price = 10
sold = 0

def output(action,units):
    global quantity,sold
    print("___")
    print("no of pencil :",action,units)
    print("Total remaining no of quantity:",quantity)
    print("Total no of sold:",sold)
    print("___")

# sell no of units of pencil 
# quantity will reduce by no of units
# sold will increase by no of units
def sell(no_of_quanty):
    """
    Docstring for sell
    
    :param no_of_quanty: Description
    # sell no of units of pencil 
    # quantity will reduce by no of units
    # sold will increase by no of units
    """
    global quantity,sold
    quantity = quantity - no_of_quanty
    sold = sold + no_of_quanty
    return no_of_quanty

# no of quanty to buy
# quantity will be increase by  no of quanty to buy
def buy(buy_units):
    global quantity 
    quantity = quantity + buy_units
    return buy_units

# revenue 
# no of quanty sold * price 
def revenue():
    global sold,price
    return sold * price

# buying 10 units
x = sell(10)
output("sell",x)

# sell another 5 units
b = sell(5)
output("sell",b)

# buying 50 units of pencil 
y = buy(50) 
output("purchase",y)

# calculate the revenue
z = revenue()
output("revenue",z)





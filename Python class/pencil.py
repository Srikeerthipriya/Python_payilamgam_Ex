Quantity = 100
price = 10
sold = 0

def revenue():
    return sold * price

def balance_Qty():
    return Quantity

def sell(x):
    Quantity = Quantity - x
    sold = sold + x
    return Quantity,sold
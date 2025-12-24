Quantity = 100
price = 10
sold = 0

def sell(Quantity,sold,x):
    Quantity = Quantity - x
    sold = sold + x
    return Quantity,sold

def revenue(a,b):
    return a * b

def balance_Qty(c):
    return c

Quantity,sold = sell(Quantity,sold,20)
print("no of sells pencil:",sold)

r = revenue(sold,price)
print("revenue of the pencil:",r)

print("remaining quantity:", balance_Qty(Quantity))

## Using global
# globals() is a built-in function that returns a dictionary of all global variables
Quantity = 100
price = 10
sold = 0

def revenue(sold,price):
    return sold * price

def balance_Qty(Quantity):
    return Quantity

def sell(x):
    global Quantity, sold
    Quantity = Quantity - x
    sold = sold + x
    return Quantity, sold

Quantity,sold = sell(20)
print("no of sells pencil:",sold)

r = revenue(sold,price)
print("revenue of the pencil:",r)

print("remaining quantity:", balance_Qty(Quantity))
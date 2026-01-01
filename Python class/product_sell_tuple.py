# pen 
pen= (200,20,0)

pencil = (100,5,0)

# output func for the product 
def output(action, units, product):
    print("no of units:",action,units)
    print("quant_after_sold:",product[0])
    print("Total of sold:",product[2])
    print("___")

# sell function for 5-pen & 2-pencil
def product_sell(product,no_of_units):
    qty,price,sold = product # unpacking
    qty -=no_of_units
    sold +=no_of_units
    product = (qty,price,sold) # packing 
    return product

x = 5 # selling 5 pens
pen = product_sell(pen,x) 

output("pen_sell:",x,pen)

y = 2 # selling 2 pencil
pencil = product_sell(pencil,2)
output("pencil_sell:",y,pencil)




# pen 
pen= (200,20,0)

pencil = (100,5,0)

# print(type(pen))

def op_pen(action,units):
    global pen
    print("no of units:",action,units)
    print("quant_after_sold:",pen[0])
    print("Total of sold:",pen[2])
    print("___")

def op_pencil(action,units):
    global pencil
    print("no of units:",action,units)
    print("quant_after_sold:",pencil[0])
    print("Total of sold:",pencil[2])
    print("___")

def pen_sell(no_of_pen):
    global pen
    qty,price,sold = pen # unpacking for the pen 
    qty = qty - no_of_pen
    sold = sold + no_of_pen 
    pen =(qty,price,sold) # packing in the pen 
    return no_of_pen

x = pen_sell(5)

op_pen("Pen_sell:",x)

# pencil sell of 2 units 


def pencil_sell(no_of_pencil):
    global pencil
    qty,price,sold = pencil 
    qty = qty - no_of_pencil
    sold = sold +  no_of_pencil
    pencil = (qty,price,sold)
    return no_of_pencil

y = pencil_sell(2)

op_pencil("pencil_sell:",y)




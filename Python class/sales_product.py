# sales of product 
# pencil , pen

# in dict , tuple & list

# tuple
# pencil 

pencil = (100,10,0)

quantity,price,sold = pencil # unpacked

print("Pencil:",quantity,price,sold)

# pen

pen= (200,20,0)

quantity,price,sold = pen 

print("Pen:",quantity,price,sold)
print(type(pen))

# sell of pencil & pen 
# no of pen = 5 & no of pencil = 2 




def ouput(action,units):
    global quantity,sold
    print("no of units:",action,units)
    print("quant_after_sold:",quantity)
    print("Total of sold:",sold)
    print("___")

def pen_sell(no_of_pen):
    global quantity,sold
    quantity = quantity - no_of_pen
    sold = sold + no_of_pen
    return no_of_pen

x = pen_sell(5)
# print ("no of pen sold:",x)
ouput("Pen_sell:",x)

# for pencil no of units sold is 2

def pencil_sell(no_of_pencil):
    global quantity,sold
    quantity = quantity - no_of_pencil
    sold = sold + no_of_pencil
    return no_of_pencil

y = pencil_sell(2)
ouput("pencil_sell:",y)





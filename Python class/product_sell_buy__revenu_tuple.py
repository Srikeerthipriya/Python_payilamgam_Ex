# pen 
pen= (200,20,0)

pencil = (100,5,0)

# output func for the product 
def output(action, units, product):
    print("no of units:",action,units)
    print("Total qauntity:",product[0])
    print("Total no of sold:",product[2])
    # print("Revenue")
    print("___")

# sell function for 5-pen & 2-pencil
def product_sell(product,sell_units):
    qty,price,sold = product # unpacking
    qty -=sell_units
    sold +=sell_units
    product = (qty,price,sold) # packing 
    return product

x = 5 # selling 5 pens
pen = product_sell(pen,x) 

output("pen_sell:",x,pen)

y = 2 # selling 2 pencil
pencil = product_sell(pencil,y)
output("pencil_sell:",y,pencil)



# buy fun 105(pen) & 12(pencil)

def product_buy(product,buy_units):
    qty,price,sold = product 
    qty +=buy_units
    product = (qty,price,sold)
    return product

z = 105 # 105 units pen is buying 
pen = product_buy(pen,z) # calling the product_buy function

# qty = 300 , buy
output("pen_buy:",z,pen) # calling the output function

a = 12 # 12 units of pencil is buying 
pencil = product_buy(pencil,a)

# qty = 110
output("pencil_buy:",a,pencil)

# revenu fun for pen & pencil
def revenu():
 
    pen_revn = pen[2] * pen[1]
    pencil_revn = pencil[2] * pencil[1]
    print( "prod_revenu_sells:",pen_revn + pencil_revn)
    # return (pen_revn + pencil_revun)
revenu()

# prod_revenu_sells = revenu()
# print("prod_revenu_sells:",prod_revenu_sells)

    




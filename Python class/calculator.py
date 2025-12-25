def add(x,y):
    return x+y

def sub(x, y):
  return x - y

def mult(x, y):
  return x * y

def div(x, y):
  return x / y

def power(x, y):
  return x ** y

def output(action,units):
    global quantity,sold
    print("___")
    print("no of pencil :",action,units)
    print("Total remaining no of quantity:",quantity)
    print("Total no of sold:",sold)
    print("___")

quantity = 100
price = 10
sold = 0

def sell(no_of_quanty):
    """
    Docstring for sell
    
    :param no_of_quanty: # sell no of units of pencil 
    # quantity will reduce by no of units
    # sold will increase by no of units
    
    """
    global quantity,sold
    quantity = quantity - no_of_quanty
    sold = sold + no_of_quanty
    return no_of_quanty
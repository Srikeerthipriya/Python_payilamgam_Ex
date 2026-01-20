def add (*args): # variable length arguments 
    total = 0
    for i in args:
        total = total + 1
    return total 

add (5,9,8,13)


## variable keywords arguments

def add (**args):
    pass 
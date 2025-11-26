# if condition 
# syntax
# if (evaluation):
# body -- print ("statement")
#mark = input("enter your score:")
#centum = 100

# if (mark >= 36):
#   print ("pass")
#    if (mark == centum):
#       print ("centum")
#else:
#   print ("fail")

m = int(input ("enter your score :"))
def evaluate_mark(m):
   

    # checking pass or fail
    if ( m >= 36 ):
        print ("pass")
    else:
        print("fail")

# Grade checking
    if ( m > 90 ):
        print ("Grade: O")    
    elif ( m > 80 ):
        print ("Grade: A")
    elif ( m > 60 ):
        print ("Grade: B")
    else:
        print ("Grade: C")

result = evaluate_mark(m)

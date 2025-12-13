# add,sub,division using function

#Arithematic Operator
#add function

def add(x, y):
  return x + y

result = add(5, 3)
print("Adding two number Sum: ", result)

#subraction in function 

def sub(x, y):
  return x - y
result = sub(5, 3)
print("Subracting two number: ",result)

#multipication  in function 

def mult(x, y):
  return x * y
result = mult(5, 3)
print("Multipying  two number: ",result)

#multipication  in function for power 

def mult(x, y):
  return x ** y
result = mult(5, 3)
print("Multipying  two number with power: ",result)

#division in function (True division)

def div(x, y):
  return x / y
result = div(5, 3)
print("Dividing  two number in true division: ",result)

#division in function (floor division)

def div(x, y):
  return x // y
result = div(5, 3)
print("Dividing  two number in floor division: ",result)

div(10,3)
result = div(10, 3)
print(result) 
## In the result it will be 3 only because it providing floor dicision 
# the same function name will overladped the function it will return the lastest function

## Comparison Operation

# less than 
def is_minor(age):
  return age < 18
result = is_minor(15)
print("Minor:", result)

# greater than 
def can_drive(age):
  return age > 18
result = can_drive(19)
print("Can drive:", result)

# equal to  
def is_centum(mark):
  return mark == 100
result = is_centum(100)
print("Centum:", result)

# not equal to  
# status = shipped, in-tracking , out for delivered , delivered
def in_progress(status):
  return status != "delivered"
result = in_progress("shipped")
print("Is in Progress:", result)

# less than  equal to  
def is_cold(temp):
  return temp <= 24
result = is_cold(18)
print("Is cold:", result)

# greater than  equal to  
def is_hot(temp):
  return temp >= 30
result = is_hot(45)
print("Is cold:", result)

## logical Operators we can't use the ! symbol for logical to check it is true or flase
#  but we can use for compare 

# and

def can_drive_legally(age,licensed):
  return age > 18 and licensed == True
result = can_drive_legally(26, True)
print("Can drive legally :" , result)

# or 

def Can_go(signal):
  return signal == "green" or signal == "yellow"
result = Can_go("green")
print("Can go :", result)

def Drink(juice):
  return juice == "apple" or juice == "orange"
result = Drink("green")
print("Can drink :", result)

# not

def is_warm(temp):
  return not is_cold(temp) and not is_hot(temp)
result = is_warm(18)
print("Can drive legally :" , result)

def is_even(num):
  return num % 2 == 0 # checking the remainder is zero or not 

def is_old(num):
  return not is_even(num) # calling the is_even function and then checking 
result = is_old(27)
print("Is odd number :", result)
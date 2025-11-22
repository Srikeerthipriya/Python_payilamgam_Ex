
# Function 
# def Function_name:
#    Expression/statement
# call() -- call the function 

# def read_write ():
#   name = input ("enter your name: ")
#print("your name : " + name)

#read_write(#)
# add,sub,division using function

def read_write (field): ## field is parameter passing the input to values to function or class 
    data = input ("enter your " + field + ":")
    print("your "+ field + " is: " + data)

read_write("name")
read_write("age")
read_write("phone no")
read_write("degree")
read_write("salary_expection")
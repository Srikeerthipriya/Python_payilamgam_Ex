## Exception handling  -- we need to know the error & we can debug it 

# age = int(input("age:"))
# age = age + 1
# print(age)

# ValueError: invalid literal for int() with base 10: 'Keerthi'

try:
    age = int(input("age:"))
    age = age + 1
    print(age)
except ValueError:
    print("invalid char,try number")
    

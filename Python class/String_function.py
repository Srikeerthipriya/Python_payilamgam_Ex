# https://docs.python.org/3/library/stdtypes.html#textseq

print(dir(str))
print(len(dir(str)))

# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 
# 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 
# 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 
# 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 
# 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 
# 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 
# 'zfill'

# slicing 

# Formate -- we will use formate mostly for template eg email we will create formate string that will placed in new
#new string variable the old string variable will not change 

# Syntax - variable_-string = "text {index value}".formate(parameter->a,b)

first = "Keerthi"
last = "Sri"
res = "Hello {0} {1}".format(first, last)
print(res)
# Hello Keerthi Sri

template_string = "Hello {0}: Greetings, Your order value={1} is {2}."
email = template_string.format("Keerthi", 100, "confirmed")
print(email)
# Hello Keerthi: Greetings, Your order value=100 is confirmed.

template_string = "Hello {name}: Greetings, Your order value={value} is {status}."
email = template_string.format(name="keerthi", status="confirmed", value=200)
print(email)
# Hello keerthi: Greetings, Your order value=200 is confirmed.

# lower, upper, title
# lower -- the test all letter will be in lower case 
codes = "Life is beautiful"
lw = codes.lower()
print(lw) 
# life is beautiful

# upper -- the test all letter will be in upper case 
up = codes.upper()
print(up) 
#LIFE IS BEAUTIFUL

# title -- the test all starting letter will be in upper case in the sentence
t = codes.title()
print(t) 
#Life Is Beautiful

# strip,lstrip,rstrip
# strip -- remove the empty spaces present on both start & end or left & right 
# user_name = input("Enter Your Name: ")
# print(len(user_name)) 

# s=print(user_name.strip()) 
# print(len(s)) 

# lstrip=print(user_name.lstrip()) ## remove the empty spaces present on left side
# print(len(lstrip)) 

# rstrip=print(user_name.rstrip()) ## remove the empty spaces present on right side
# print(len(rstrip))   

#  split,rsplit ,splitlines  
# split
# fruit, qty, price, variant
tokens = "apple,20,4,green".split(",")
print(tokens)

# rsplit -- rsplit(sep, maxsplit)
token = "apple,20,4,green".rsplit(",",2) # it will split from right side with the no we mention 
print(token)

#splitlines()
tok = "Life is \nbeatuiful".splitlines() # it will split the lines 
print(tok)

# startsWith, endswith
course_one = "be - CS"  # User Input
course_two = "BSC - CS"

if course_one.upper().startswith("BE"):# check the starting word
    print("Engineer")
else:
    print("Non Engineer")


if course_one.lower().endswith("cs"):# check the ending word
    print("CS Graduate")

if course_two.endswith("cs"):
    print("CS Graduate")

# find
data = "my name is keerthi"
res = data.find("name") # it will find the first index value of the given word or letter 
print(res)

# count
data = "my name is keerthi"
res = data.count("m") # it's provide the no of count of the letter or word in 
print(res)

# join
data = "orange     apple"
tokens = data.split() # default it will split with space
print(tokens)
out_one = " ".join(tokens) # join with space
out_two = ",".join(tokens) # join with comma

print(out_one)
print(out_two)

# replace
data = "orange, aple"
res = data.replace("aple", "apple") # replace that word with what we need
print(res)


# # iterate
message = "orange apple"
for c in message: # it will print each letter line by line
    print(c)


# slicing [start:end:step]

msg = "nothing is impossible"
print(msg)
print(len(msg))

print(msg[0:7]) # print the letter present between 0 to 6 -- start include end  is exclusive 

print(msg[0:5])

print(msg[-1:-8]) # start from last from and end index exclusive with end 


print(msg[::-1]) # print the string reverse order

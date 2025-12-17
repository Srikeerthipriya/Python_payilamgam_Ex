# 1)without using in bluit function 

n = [1,2,3,4,5]
rotate = 1

li=len(n)-1 # find the last index number 

for i in range(rotate): # loop till the range of rotation 

    fi=n[0] # find the 1st value

    for x in range(li): # loop till last index 
        n[x]=n[x+1] # assign the 1st value the index(0) to next index(1) 
    n[li]=fi # assign the first value to last_index(li)

print("1nd rotation anticlock wise:",n)

# 2)using bluit in function 

num=[1,2,3,4,5]
rotate = 1

for i in range(rotate):
    first = num.pop(0) # remove the first value
    num.append(first) # add the first value at last

print("Bluit in function for 1st rotation anticlock wise:",num)


# 3) using slicing
n = [1,2,3,4,5]

# for 2 rotation clock wise slicing

# a = n[3:]
# b = n[0:3]

# print("clock wise 2rotate using slicing",a+b)

# clock wise 2rotate using slicing

a = n[0:1]
b = n[1:5:1]

print("clock wise 2rotate using slicing:",b+a)
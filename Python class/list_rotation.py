num = [1,2,3,4,5]

# 1) 1 rotation with out using in bluit function 

rotate = 1 # no of tmes to rotate 

for i in range(rotate): # loop end till the no rotation 

    li = len(num) - 1  # to find the last index 
    z = num[li]  # assign the last index value of list in variable z

    for x in range(li,0,-1): # loop start at the last index and end at the start step will be reverse 

        num[x] = num[x-1] # last index value assign to next  last index 

    num[0] = z # assign the 1st index value to the variable z

print("1st rotatation:",num)


# 1) 1 rotation with using bluit in function 

num = [1,2,3,4,5]
rotate = 1 
for i in range(rotate):

    x = num.pop() # remove the last value 
    num.insert(0,x) # insert the removed last value in first index (0)

print("1st rotate using bluitin function:",num)


# 2) 2 rotation without using bluit in function 

num2 = [1,2,3,4,5]
rotate = 2
for i in range(rotate):

    li=len(num2)-1
    z=num2[li]

    for x in range(li,0,-1):
        num2[x]=num2[x-1]
    num2[0]=z

print("2nd rotation:",num2)

# 2) 2 rotation using bluit in function 
num2 = [1,2,3,4,5]
rotate = 2
for i in range(rotate):

    x=num2.pop()
    num2.insert(0,x)

print("2nd rotation using bluit in function:",num2)

# 3) 3 rotation using bluit in function 

num3 = [1,2,3,4,5]
rotate = 3
for i in range(rotate):

    li=len(num3)-1
    z=num3[li]

    for x in range(li,0,-1):
        num3[x]=num3[x-1]
    num3[0]=z

print("3nd rotation:",num3)

# 2) 3 rotation using bluit in function 

num3 = [1,2,3,4,5]
rotate = 3
for i in range(rotate):

    x=num3.pop()
    num3.insert(0,x)

print("3nd rotation using bluit in function:",num3)


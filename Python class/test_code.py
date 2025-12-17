num2 = [1,2,3,4,5]
rotate = 2
for i in range(rotate):

    li=len(num2)-1
    z=num2[li]

    for x in range(li,0,-1):
        num2[x]=num2[x-1]
    num2[0]=z

print("2nd rotation:",num2)
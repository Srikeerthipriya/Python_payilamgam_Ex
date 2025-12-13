# for <variable> in <sequence>:
#     <code>
# we can use the for loop only we know the terminatation/end 
row = int(input("enter the row:"))
for i in range(1,row+1,1):
    print ("* " * row)

#row = int(input("enter the row:"))
for r in range(1,row+1,1):
    print ("* " * r)

#row = int(input("enter the row:"))
for r in range(row,0,-1):
    print ("* " * r)
# add the numbers in the list
num = [10,12,1,6,3,5,4]
sum=0
for i in num:
    sum += i
    # print(sum)
print(sum)


n =[4,3,2,1]
sum=0
for i in n:
    sum += i
print(sum)

# print odd number in the list 

n = [3,5,4,2,22,30,7,26]
odd =[]

for i in n:
    if (i%2)!=0 :
        odd.append(i)
print(odd)

# print(dir(list))

# find the number is in the list 
num = [3,6,8,9]
for i in num:
    if(i == 11):
        print(True)
else:
    print(False)

# square of the given number in the list & output in list 
num = [3,6,8,9]
square_num = []  
for i in num:

    square = i * i
    square_num.append(square)   

print(square_num)




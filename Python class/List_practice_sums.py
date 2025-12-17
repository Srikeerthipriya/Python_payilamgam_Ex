# # loops sums

# #1) sum of odd 

num = [2,6,3,7,9,25,89,34]
sum =0  
odd =[] 

for i in num:
 
    if i % 2 != 0:
        odd.append(i)
print("odd number:",odd)

for i in odd:
        sum +=i
print("sum of odd no:",sum)

# #2) multiples of even 

mul =1
even = []

for i in num:
     
     if i % 2 ==0:
         even.append(i)
print("even no:",even)

for i in even:
     mul *=i
print("multiple of even no:",mul)

# #3) print odd & even number

odds=[]
evens=[]

for i in num:
     if i % 2 !=0:
         odds.append[i]
         
     elif i % 2 ==0:
         even.append[i]

print("odd number:",odds)
print("even no:",evens)

#4) provide the multiple of 3 for given list 

mults =[]
for i in num:
     mult =3*i
     mults.append(mult)
print("Multi of 3:",mults)
     

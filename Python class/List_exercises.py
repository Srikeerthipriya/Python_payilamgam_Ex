# 15/DEC/2025) List

# Input: [56, 54, 100, 35, 83, 81, 100, 66, 93, 81, 79, 67, 100, 50, 74, 59, 100, 61, 37, 60]

# 1) Given math scores, find how many scored centum: 100

marks = [56, 54, 100, 35, 83, 81, 100, 66, 93, 81, 79, 67, 100, 50, 74, 59, 100, 61, 37, 60]

# creating empty list centum
centum =[]

# checking each score is centum or not 
for i in marks:
    if i == 100:
        #print(i)
        # adding all the centum score in the centum list 
        centum.append(i)
# print the centum list 
print(centum)
# print the no of centum in the list 
print("No of centum:",len(centum))

#2) Given scores, grade each score: A > 90, B > 80, C > 60, others D

Grade_A =[]
Grade_B =[]
Grade_C =[]
Grade_D =[]

# getting each score is iterated
for i in marks:
    # check the score which is greater then 90
    if (i>90):
        # adding all the score which is greater than 90 in grade_A list
        Grade_A.append(i)

    elif (i>80):
        Grade_B.append(i)
        
    elif (i>60):
        Grade_C.append(i)
        
    else:
        Grade_D.append(i)
       
print("Grade A scores:",Grade_A)
print("Grade B scores:",Grade_B)
print("Grade C scores:",Grade_C)
print("Grade D scores:",Grade_D)

#3) Given scores, count students for each grade

print("No of students score Grade A:",len(Grade_A))
print("No of students score Grade B:",len(Grade_B))
print("No of students score Grade C:",len(Grade_C))
print("No of students score Grade D:",len(Grade_D))

#4) Given numbers, reverse numbers [1, 2, 3] -> [3, 2, 1]

# Bluit in function
num = [1,2,3]
num.reverse()
print("Reverse no using reverse method:",num)

# without using bluit in function using range

nums =[1,2,3,4,5]
reverse_num=[]

for i in range(len(nums) -1,-1,-1):
    reverse_num.append(nums[i])
print("Reverse no using range:",reverse_num)

# without using bluit in function using scling

no = [1,2,3,4,5,6]
reverse_no = no[::-1]
print(reverse_no)


#5) Given numbers, rotate them in place N times [1, 2, 3, 4, 5] -> [4, 5, 1, 2, 3]

N = [1,2,3,4,5]





#4) Given numbers, double them in place [1, 2, 3, 4, 5] -> [2, 4, 6, 8, 10]
n = [1,2,3,4,5]

mult_2 =[]

for i in n:
    mult = i * 2
    mult_2.append(mult)
print("mult of 2:",mult_2)
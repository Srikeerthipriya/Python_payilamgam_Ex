
num = [2,4,14,15,3,6,5]

def filter (num,condition): # filter fun is calling the lambda x & lambda y funcs
    res=[]
    for i in num:
        if(condition(i)): # pass the parameter condtion 
            res.append(i) # add the no in res list
    return res

# 1)find 1st multiple of 5

first_mult_5 = filter(num,lambda x:x%5==0)[0]
print(first_mult_5)

# 2)find all multiple of 5

mult_5 = filter(num,lambda x:x%5==0)
print(mult_5)

# n = [1,2,3,4,5,6,7,8,9,10]


# def filter (condition): # filter fun is calling the lambda x & lambda y funcs
#     res=[]
#     for i in n:
#         if(condition(i)): # pass the parameter condtion 
#             res.append(i) # add the no in res list
#     return res

# table_2 = filter(lambda x:x*2)
# print(table_2)



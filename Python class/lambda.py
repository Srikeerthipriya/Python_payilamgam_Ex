# fun -- f(x)=x+y
# f(f(x)=f(x)) -- higher order function 

n = [10,12,3,4,5,6,8,9]

def filter (n,condition): # filter fun is calling the lambda x & lambda y funcs
    res=[]
    for i in n:
        if(condition(i)): # pass the parameter condtion 
            res.append(i) # add the no in res list
    return res
e = filter(n,lambda x:x%2==0) # using lambda fun we are checkimg the condtion for even no 
print("even_num",e)
o = filter(n,lambda y:y%2!=0) # using lambda fun we are checkimg the condtion for odd no 
print("odd_num",o)



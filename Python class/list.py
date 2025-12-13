#   lists -- Oredered collection with out any limitation --of data elements

# int, float, string, boolean -> primitive data types

# list -> list of numbers, list of floats, list of strings, etc... -> composite data types

#print(dir(list)) ## list functions 

## 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# create a list 
# using square braket[]

num = [1,2,3,4,5]
print(num)
print(type(num))

# directly mention the list
n = list(range(0,6))
print(n)
print(type(n))

# 1.append - add the last in the list
num.append("a")
print(num)

# 2.clear - clear the enter list but there wll the empty list 
cl=num.clear()
print(cl)

# 3.copy - Returns a shallow copy of the list in new list
old_list = [3,4,5,6]
new_list = old_list.copy()
print(new_list)

# # 4.count() -- Counts how many times a value appears.
text = [1,"a",2,"b","a",3,2,4,1]
print(text.count(3))

# # 5.extend -- Adds elements of another list to the end.
ad=[1,2,3]
add_list=ad.extend([0,7])
print(ad)

# 6.index - Returns the index of the first occurrence of a value.
ads=[1,2,3,2,4]
print(ads.index(2))

# # 7.insert(index,value) # insert the value in given index value 
ads=[1,2,3,2,4]
ads.insert(2,9) 

#  print(ads)

#8.pop() -- remove the last value
re=ads.pop() # parameter is index value -- pop (index value )
print(re)

# 9.remove() - Removes the first occurrence of a value. -- remove the value in parameter
print(num)
a =num.remove(3)
print(a)
print(num)

# 10.reverse() - Reverses the list in-place. -- modify the value in same memory location 
q = [1,2,3,4,5]
print(q)
q.reverse()
print(q)

# 11.sort() - Sorts the list in ascending order.
asc = [2,3,1,5,2,6]
print(asc)
asc.sort()
print(asc)

# length of list
print(len(num))

#sum 
print(sum(num))
# print(sum(text))
# print(dir(list)) 


n = [1,3,9,5,8,0]

# 1) append () -- mention value add at end of the list

n.append("a") # adding at the end 

print("append the a at last",n)

# 2) pop

n.pop() # remove the last value default last index
print("pop - removing the last value :",n)

n.pop(0) #  remove the 1st value here the index value is (0) -
# pop we need to mention the index number

print("pop(0) - remove the 1st value:",n)

# 3) insert(index,value) # insert the value in given index value 

n.insert(0,"a")
print("insert (a) variable at 1st index(0)",n)

# 4) reverse() -- reverse the list in place -- modify the value in same memory location 

n.reverse()
print("reverse list in place:",n)

# 5) sort() -- default sort the no in ascending order
# if sort the list connect both string & integer it's not supporting

no = [8,3,5,0,1,9,5]

no.sort()
print("sort in ascending order:",no)

# 6) sorted() -- ascending order the list in new list 
# so ne need to creat new list

nos = [8,3,5,0,1,9,5]
asc_no = sorted(nos)
print("sort in ascending order:",asc_no)

# 7) sorted() -- descending pass the reverse = True

des_no = sorted(nos,reverse=True)
print("sort in descending order:",des_no)

# num = {1,2,3,4,5}
# char ={}
# print(type(num))
# print(type(char))


# methods
# print(dir(set)) 

# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 
# 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 
# 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'


odd = {1,3,5,7}
even = {2,4,6,8,10}


m3 = {3,6,9,12,15}
m6 = {2,4,6,8,10,12}

# # m3 - m6 -- difference 
# print(set.difference(m3,m6))

# # m6 - m3
# print(set.difference(m6,m3))

# # common in both  sets 
# print(set.intersection(m3,m6))

# m3 & m6 -- union 
print(set.union(m3,m6))



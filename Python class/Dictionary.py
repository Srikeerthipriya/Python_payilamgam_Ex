# Dictionary - { }
# dic = {"key": value}
# mutuable 
# unique kyes 
# methods - get,update




#print (dir(dict))

#['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__',
#  '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
# '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
#  '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', 
# '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__',
#  '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__']

# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 
# 'setdefault', 'update', 'values'

scores = [56, 54, 100, 35, 83, 81, 100, 66, 93, 81, 79, 67, 100, 50, 74, 59, 100, 61, 37, 60]

#grades ={}
grades =[]
def get_grade(marks): # create fun get_garde
    if marks >90:
        return "A"
    if marks >80:
        return "B"
    if marks >60:
        return "C"
    else:
        return "D"
    
# for score in scores:
#     grade = get_grade(score)
# #     #print(grade)
# #     grades.append(grade)

# # print(scores)
# # print(grades)
   
for score in scores: # get scores & grade the score 
    grade =get_grade(score)
    
    x = {"Score":score,"Grade":grade} # provide variable 
    grades.append(x)
print(grades)

# for score in scores: # get scores & grade the score 
#     grade =get_grade(score)
    
#     grades.update({"Score":score,"Grade":grade}) # provide variable 
#     #grades.append(x)
# print(grades)
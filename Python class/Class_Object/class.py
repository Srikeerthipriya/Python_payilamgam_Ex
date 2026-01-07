class Employee: # declaring the class 
    
    def __init__(self,first_name,last_name,salary):
        self.first = first_name  ## first 
        self.last = last_name 
        self.salary = salary

    def name(self): # we are calling the full -- must give the parameter self
        print(self.first,self.last)

    def increment(self,value):
        self.salary = self.salary + value
        print(self.salary)


# object / instance of employee -- e_one 
e_one= Employee ("Keerthi","Shankar",50000) # here only we are creating the class employee 
# print(e_one.first,e_one.last) ## first the name should be name 
e_one.name() #we no need to pass the parameter it will call automaticatlly
e_one.increment(10000)


e_two = Employee("Nikshi","P",60000)
#print(e_two.first,e_two.last)
e_two.name()
e_two.increment(10000)



# employee() -- instantiation / constructed 
#print(type(e_one))

# o/p - <class '__main__.employee'> 
# -- main -- envinorment (currently which file we running) 
#  employee -- class name 


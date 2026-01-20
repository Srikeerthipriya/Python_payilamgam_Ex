class Student:
    
    def __init__(self,first_name,last_name,ID):
        self.first = first_name
        self.last = last_name
        self.id = ID
        self.name = self.first + self.last
        print (self.name)

        

    def hello(self):
        print("My name is",self.name)


stu_1 = Student("Sri","Keerthi",24)
stu_1.hello()

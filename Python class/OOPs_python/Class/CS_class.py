class Dept:

    def __init__(self,name,year):
        self.name = name 
        self.year = year
        self.students = []

    def add_stu(self,name,id):
        student = Stu(name,id)
        self.students.append(student)

    def add(self,student):
        self.students.append(student)


    def get_all(self):
        return self.students

    def get_dept_details(self):
        print("Dept Name:",self.name,"Dept year:",self.year)

    def remove_stu(self,id):
        pass

    def get_stu(self,id):
        pass



class Stu:

    
    def __init__(self,name,id):
        self.name = name
        self.id = id
        
    def __str__(self):
        return self.name +" " +str(self.id)
    
    
    def get_stu_details(self):
        print("Name:",self.name,"Stud_ID:",self.id)
        

        
dep_1 = Dept("computer Science",2026)


stu_1 = Stu("Keerthi",101)
stu_2 = Stu("Nikshi",102)
stu_3 = Stu("Virddhi",103)
stu_4 = Stu("Shankar",104)
stu_5 = Stu("Shri",105)


dep_1.add(stu_1)
dep_1.add(stu_2)
dep_1.add(stu_3)
dep_1.add(stu_4)
dep_1.add(stu_5)

dep_1.add_stu("keerthi",101)
dep_1.add_stu("nikshi",102)

x = dep_1.get_all()
print(x)

for i in x:
    print(i)

dep_1.get_dept_details()



# dep_3 = Dept("ECE",2026)
# dep_4 = Dept("Mech",2026)



# dep_3.get_dept_details()
# dep_4.get_dept_details()


# stu_5 = Stu("Shri",105)
# stu_6 = Stu("Nithathi",106)
# stu_7 = Stu("Subbu",107)
# stu_8 = Stu("Sandy",108)
# stu_9 = Stu("Gulfi",109)
# stu_10 = Stu("Mini",110)
# stu_11 = Stu("Swetha",111)
# stu_12 = Stu("Subha",112)
# stu_13 = Stu("Guru",113)
# stu_14 = Stu("Vaishu",114)
# stu_15 = Stu("Vimala",115)


# stu_1.get_stu_details()
# stu_2.get_stu_details()
# stu_3.get_stu_details()
# stu_4.get_stu_details()
# stu_5.get_stu_details()
# stu_6.get_stu_details()
# stu_7.get_stu_details()
# stu_8.get_stu_details()
# stu_9.get_stu_details()
# stu_10.get_stu_details()
# stu_11.get_stu_details()
# stu_12.get_stu_details()
# stu_13.get_stu_details()
# stu_14.get_stu_details()
# stu_15.get_stu_details()   




# add student -- id , name 

# remove student id 

# Get all student id in []

# Get all student name & id in []

# dep_2 = Dept("IT",2026)

# dep_2.add_stu("nikshi",102)

# y = dep_2.get_all()

# for i in y:
#     print(i)

# dep_2.get_dept_details()
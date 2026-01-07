#1) Get marks for all 5 subjects
#2) calculate the total
#3) Find the top score 
#4) Find pass or fail 
#5) find subject with centum score 
#6) calculate the percentage 
#7) calculate the cut off (Maths,phy,chem)

#1) Get marks for all 5 subjects

def get_marks():
    subjects = ["Maths", "Physics", "Chemistry", "English", "Tamil"]
    marks = {}

    for sub in subjects:
        marks[sub] = int(input("Enter marks for {sub}: "))
    return marks
marks = get_marks()

def calculate_total(marks):
    return sum(marks.values())


def find_top_score(marks):
    return max(marks.values())


def pass_or_fail(marks):
    for score in marks.values():
        if score < 35:
            return "FAIL"
    return "PASS"


def centum_subjects(marks):
    return [sub for sub, score in marks.items() if score == 100]


def calculate_percentage(total):
    return (total / 500) * 100


def calculate_cutoff(marks):
    return marks["Maths"] + marks["Physics"] + marks["Chemistry"]



marks = get_marks()

total = calculate_total(marks)
top_score = find_top_score(marks)
result = pass_or_fail(marks)
centum = centum_subjects(marks)
percentage = calculate_percentage(total)
cutoff = calculate_cutoff(marks)

print("\n----- RESULT -----")
print("Marks:", marks)
print("Total:", total)
print("Top Score:", top_score)
print("Result:", result)
print("Centum Subjects:", centum if centum else "None")
print("Percentage:", round(percentage, 2), "%")
print("Cut Off (Maths + Physics + Chemistry):", cutoff)




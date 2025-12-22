s1 ={"math":98,
     "tamil":70,
     "eng":65,
     "science":55,
     "social":85}

s2 ={"math":88,
     "tamil":60,
     "eng":55,
     "science":75,
     "social":90} ## packing 

s3 ={"math":60,
     "tamil":40,
     "eng":55,
     "science":40,
     "social":75}

scores =[s1,s2,s3]

# for score in scores:
#     value = score.get("tamil")
#     mark = value + 10
#     score.update({"tamil":mark})

# def get_tamil (mark):
#     tamil= mark.get("tamil")
#     return tamil

# def set_tamil (mark,value):
#     mark.update({"tamil":value})


# for score in scores:
#     value = get_tamil(score)
#     value +=10
#     set_tamil(score,value)

def get_avg(math,tamil,eng,science,social):
    # math = score.get("math")
    # tamil = score.get("tamil")
    # eng = score.get("eng")
    # science = score.get("science")
    # social = score.get("social")

    avg = (math+tamil+eng+science+social)/5
    return avg

for score in scores:
    avg = get_avg(**score) # unpacking -- dic is ** -- it will the get the value 

    score.update({"pet":avg})
    
    mark=score.values() # we will the marks of all subjects

    print("marks of each student",mark)

print(scores)

# list all avg panu 

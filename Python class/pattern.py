#no of stars and rows is same

row = int(input("Enter number of stars & rows: "))

i = 1
stars = 5

while i <= row:
    print("*" * stars)
    i =i + 1

# increase the stars one by one in each row & column
row = int(input("Enter number of increase rows: "))

i = 1
stars = 1

while i <= row:
    print("*" * stars)
    stars =stars + 1
    i =i + 1

# decrease the stars one by one in each row & column
row = int(input("Enter number of decrease rows: "))

i = row
#stars = 1

while i > 0:
    print("*" * i)
    #stars =stars - 1
    i =i - 1




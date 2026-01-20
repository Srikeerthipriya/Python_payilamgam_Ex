file = open("D:\Payilagam\Product.csv")

# print(file.readline())

first_line = file.readline()
pro_tuple = tuple(first_line.split(','))
print("First line :",pro_tuple)

second_line = file.readline()
pen_tuple = tuple(second_line.split(','))
print("Second line :",pen_tuple)

third_line = file.readline()
pencil_tuple = tuple(third_line.split(','))
print("Second line :",pencil_tuple)

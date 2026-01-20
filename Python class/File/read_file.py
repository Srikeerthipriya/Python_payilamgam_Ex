file = open("D:\Payilagam\Product.csv")

# print(file.read()) ## read all the content 

print(file.readline()) ## read the 1st line

print(file.readlines()) ## read all the lines in list 

# file.write("hello") -- error - io.UnsupportedOperation: not writable

file.close() # closing the file 
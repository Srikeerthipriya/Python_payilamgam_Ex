# #1)    I am going to school
# #   O/p - I am going to School

# # bulit_in_function
text ="I am going to school" 
#print(text.split())
wrd = text.split()
print(wrd)

# capitailaze the 1st letter in 1st word & 1letter in last word
wrd[0] = wrd[0].capitalize()
wrd[-1] = wrd[-1].capitalize()
# sequence item 0: expected str instance, builtin_function_or_method found
crt_text = " ".join(wrd) 
print(crt_text)

# #2) hi how are you 
# #    o/p - Hi How Are You

msg2 = "hi how are you "
print(msg2)
# capitailaze the 1st letter in all the words
print("Msg2 :",msg2.title())


#3) How are You 
#   woH are uoY
Greeding = "How are You"
grd = Greeding.split()
print(grd)

# reverse the 1st & last word
for i in range(len(grd)):
    if i % 2 == 0:
       grd[i]=grd[i][::-1]
 
greeds = " ".join(grd)
print(greeds)

# print(type(reverse_grd))
# for i in grd:
#     rev = grd[1:4:-1]
#     rev = grd[-1:-4:-1]
#     reverse_grd.append(rev)
# print(reverse_grd)

# #TypeError: sequence item 0: expected str instance, list found
# output =" ".join(reverse_grd)
# print(output)


# 4) i/p - Sri Keerthi Priya
#    o/p - irS ihtreeK ayirp 

name = "Sri Keerthi Priya"
first_name = name.split()
print(first_name)

# reverse each word
for i in range(len(first_name)):
     first_name[i]= first_name[i][::-1]

#join the reversed each word
reverse_name =" ".join(first_name)
print(reverse_name)

# 5) i/p - Sri Keerthi Priya
#    o/p - Priya Keerthi Sri 

names = "Sri Keerthi Priya"
#reverse the each word in same word by index value using slicing 
nam = names.split()[::-1]
print(nam)

reverse_nam=" ".join(nam)
print(reverse_nam)














# 5) i/p - Sri Keerthi Priya 
#    o/p - Priya Keerthi Sri 
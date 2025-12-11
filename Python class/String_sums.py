#1)    I am going to school
#   O/p - I am going to School


# bulit_in_function
# text ="I am going to school" 
# #print(text.split())
# wrd = text.split()
# #print(wrd)

# # capitailaze the 1st letter in 1st word & 1letter in last word
# wrd[0] = wrd[0].capitalize
# wrd[-1] = wrd[-1].capitalize
#sequence item 0: expected str instance, builtin_function_or_method found
# crt_text = " ".join(wrd) 
# print(crt_text)

#2) hi how are you 
#    o/p - Hi How Are You

msg2 = "hi how are you "
print(msg2)
print("Msg2 :",msg2.title())


#3) How are You 
#   woH are uoY
Greeding = "How are You"
grd = Greeding.split()
print(grd)


reverse_grd = []
print(type(reverse_grd))
for i in grd:
    rev = grd[::-1]
    reverse_grd.append(rev)


# TypeError: sequence item 0: expected str instance, list found
# output =" ".join(reverse_grd)
# print(output)
text = "life is beautiful"
text2 = "   python   "
numbers = "12345"
mixed = "keer24"
title_str = "Life is Beautiful"
tabs = "A\tB\tC"
words = ["apple", "banana", "cherry"]

# 1. capitalize()
print("capitalize:", text.capitalize()) # capital the first letter in the sentence

# 2. casefold()
print("casefold:", "HELLO".casefold()) # change all the letter to lowercase

# 3. center() -- center(width, fillchar)
print("center:", text.center(50, " ")) # center the text 

# 4. count()
print("count:", text.count("l")) # provide the count of the letter

# 5. encode()
print("encode:", text.encode()) #Converts a string to bytes.

# 6. endswith()
print("endswith:", text.endswith("beautiful")) # checking the ending wordsb

# 7. expandtabs()
print("expandtabs:", tabs.expandtabs(4)) # Replaces \t with spaces.

# 8. find()
print("find:", text.find("world")) # find the letter index in the sentence

# 9. format()
print("format:", "My name is {}".format("Alice")) # format throught string directly

# 10. format_map()
print("format_map:", "{name} is {age}".format_map({"name": "Bob", "age": 25})) # formate throught index name

# 11. index()
print("index:", text.index("is")) # provide the index value of the word

# 12. isalnum()
print("isalnum:", mixed.isalnum()) # Checks if all characters are letters or numbers.

# 13. isalpha()
print("isalpha:", "Hello".isalpha()) #Checks if all characters are letters.

# 14. isascii()
print("isascii:", "Hello".isascii())

# 15. isdecimal()
print("isdecimal:", numbers.isdecimal()) #Checks if characters are decimal digits.

# 16. isdigit()
print("isdigit:", numbers.isdigit())# Checks if characters are digits

# 17. isidentifier()
print("isidentifier:", "my_var".isidentifier()) # Checks if a string is a valid Python variable name.

# 18. islower()
print("islower:", text.islower())# Checks if all letters are lowercase.

# 19. isnumeric()
print("isnumeric:", "⑤".isnumeric()) # Checks for numeric characters

# 20. isprintable()
print("isprintable:", "Hello\n".isprintable()) # Checks if all characters are printable.

# 21. isspace()
print("isspace:", "   ".isspace()) # Checks if string contains only whitespace

# 22. istitle()
print("istitle:", title_str.istitle()) # Checks if each word is capitalized.

# 23. isupper()
print("isupper:", "HELLO".isupper()) # Checks if all letters are uppercase.

# 24. join()
print("join:", "-".join(words)) # join the words with -

# 25. ljust() -- ljust(width, fillchar)
print("ljust:", text.ljust(20, ".")) # Left-aligns string with padding.

# 26. lower()
print("lower:", "HELLO".lower()) # Converts to lowercase.

# 27. lstrip()
print("lstrip:", text2.lstrip()) # remove the left side space

# 28. maketrans() + translate()
table = str.maketrans({"a": "1", "e": "2"}) # Used together to replace characters.
print("maketrans/translate:", "apple".translate(table))

# 29. partition()
print("partition:", text.partition(" ")) # Splits into 3 parts: before, separator, after.

# 30. removeprefix()
print("removeprefix:", "SriKeerthi".removeprefix("Sri")) # Removes prefix if present.

# 31. removesuffix()
print("removesuffix:", "SriKeerthi".removesuffix("Keerthi")) # Removes suffix if present.

# 32. replace() # replace(old, new)
print("replace:", text.replace("world", "Python")) # replace the word with what we want

# 33. rfind()
print("rfind:", "hello hello".rfind("hello")) # Finds last occurrence (rightmost).

# 34. rindex()
print("rindex:", "hello hello".rindex("hello")) # Like rfind but error if not found.

# 35. rjust() -- rjust(width, fillchar)
print("rjust:", text.rjust(20, ".")) # Right-aligns with padding.

# 36. rpartition()
print("rpartition:", "a b c".rpartition(" ")) # Like partition but splits from the right.

# 37. rsplit()
print("rsplit:", "a,b,c".rsplit(",", 1)) # Splits from the right.

# 38. rstrip()
print("rstrip:", text2.rstrip()) # Removes right side spaces

# 39. split()
print("split:", "a,b,c".split(",")) # Splits into a list.

# 40. splitlines()
print("splitlines:", "Hello\nWorld".splitlines()) # Splits at newlines.

# 41. startswith()
print("startswith:", text.startswith("life")) # Checks if string starts with something.

# 42. strip()
print("strip:", text2.strip()) # Removes front & back spaces.

# 43. swapcase()
print("swapcase:", "Hello World".swapcase()) # Swaps uppercase ↔ lowercase.

# 44. title()
print("title:", text.title()) # Capitalizes each word.

# 45. translate()  (already used above but shown again)
print("translate:", "abc".translate(str.maketrans("abc", "123"))) # Transforms characters using a translation table.

# 46. upper()
print("upper:", text.upper()) # Converts to uppercase.

# 47. zfill()
print("zfill:", "42".zfill(5)) # fill left with zeros.

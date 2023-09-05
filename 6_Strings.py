# Python Strings: Modification, Slicing, Concatenation, Formatting & String methods

aString = "This is a string."
bString = 'This also is a string.'

cString = """This is a multiline string,
which can contains strings on multiple lines
like this."""

""" String Slicing """
print(aString[2:5])  # [start index, end index, step]
print(aString[:5])  # This will start at index 0 & print everything upto Index 4
print(aString[2:])  # This will start at index 2 and print everything after that

""" Python - String Modification """
# .upper() method
temp = aString.upper()
print(temp)

# .lower() method
temp = aString.lower()
print(temp)

# .strip() method to remove whitespaces from beginning or end
temp = "    this string has whitespaces.   "
print(temp)
print(temp.strip())

# .replace() method to replace string with another string
temp = "Hellow World..."
print(temp.replace(".", "!", 1))  # (String to be replaced, string to be replaced with, instances to be replaced)
print(temp.replace(".", "!"))

# .split() method to split string into substrings with a delimiter
temp = aString.split(" ")
print(temp)

# String concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

""" Python - String Formatting """
cRoll = 52
temp = "I am Rohit and my Roll is {}"
print(temp.format(cRoll))
# multiple placeholder formatting
place = "Mumbai"
siblingCount = 3
temp = "I am Rohit and my Roll is {}, I live in {} and have {} siblings."
print(temp.format(cRoll, place, siblingCount))
# Using indexes to format a string
temp1 = "I am Rohit and my Roll is {0}, have {2} siblings & I live in {1}."
print(temp1.format(cRoll, place, siblingCount))

"""Escape Characters in python String:"""
# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value

""" Python - String Methods """
temp = "this is how we Use String methods!!"

# (1) .capitalize() method to convert first character to Upper Case
print("use of .capitalize() method")
print(temp.capitalize())

# (2) .casefold() method to convert string to lower case
print("use of .casefold() method")
print(temp.casefold())

# (3) .center() to change alignment of string to center
print("use of .center() method")
print(temp.center(100))  # .center(length)
print(temp.center(100, "_"))  # .center(length, filler character)

# (4) .count() method to count the number of occurrence of a string in a string
print("use of .count() method")
print(f"number of times \"e\" occurred in \"{temp}\": {temp.count('e')}")

# (5) .encode() method to return an encoded version of a string (not used very often)
enc = "MyPassword".encode()
print(enc)

# (5) .index() method to return index of a string in a string
print("use of .index() method")
print(temp.index("U"))

# (6) .isalnum() : method to check if all character in a string are alphanumerics
# (7) .isalpha() : method to check if all characters in a string are alphabets
# (8) .isascii() : method to check if all characters in a string are ASCII characters
# (9) .isdecimal() : method to check if all characters in a string are decimals
# (10) .isdigit() : method to check if all characters in a string are digits
# (11) .isidentifier() : method to check if string is an identifier
# (12) .islower() : method to check if all characters in a string are in lower case
# (13) .isupper() : method to check if all characters in a string are in upper case
# (14) .isnumeric() : method to check if all characters in a string are numbers
# (15) .isprintable() : method to check if all characters in a string are printable
# (16) .istitle() : method to check if a string follows the rule of a title
# (17) .isspace() : method to check if all characters in a string are whitespaces
# (18) .join() : method to join substrings with or without a seperator
print("use of .join() method")
tempTuple = ("Google", "Is", "in", "USA")
tempStr = " ".join(tempTuple)
print(tempStr)

# (19) .ljust() : method to return a left justified string
print(tempStr.ljust(50, "*"))  # ljust(length, filler character)
# (20) .rjust() : method to return a right justified string

# (21) .lstrip() : method to return left trimmed version of a string
# (22) .rstrip() : method to return right trimmed version of a string

# (23) .maketrans() : method to return a translation table to be used in translations
print("use of .maketrans() method")
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)  # Syntax : .maketrans(String to replace, replacement string, strings to be removed)
print(txt.translate(mytable))

# (24) .partition() : Searches for a substring & return a tuple i.e. ("Before match", "Matched", "After match")
print("use of .partition() method")
temp = "I could eat bananas all day and eat"
tempTup = temp.partition("bananas")
print(tempTup)

# (25) .rfind() : Searches the string for a specified value and returns the last position of where it was found
print("use of .rfind() method")
x = temp.rfind("eat")
print(x)

# (26) .rindex() : Searches the string for a specified value and returns the last position of where it was found
# (27) .rpartition() : Returns a tuple where the string is parted into three parts, search is done from right end.
# (28) .splitlines() : Splits the string at line breaks and returns a list
print("use of .splitlines() method")
temp = "Thank you for the music\nWelcome to the jungle"
splitList = temp.splitlines()
print(splitList)

# (29) .swapcase() : Swaps cases, lower case becomes upper case and vice versa
# (30) .zfill() : Fills the string with a specified number of 0 values at the beginning
txt = "50"
x = txt.zfill(10)  # string.zfill(len)
print(x)


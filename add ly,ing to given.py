# 52. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given
# string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3,
# leave it unchanged. Go to the editor
# a. Sample String : 'abc'
# b. Expected Result : 'abcing'
# c. Sample String : 'string'
# d. Expected Result : 'stringly'

name=input("enter the name")
a="ly"
b="ing"
if name!=name+b:
    print(name+a)
elif name!=name+b:
    print(name+b)
else:
    print(name+b+a)
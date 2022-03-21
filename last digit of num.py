# 33. Write a program to display the last digit of a number.

num=int(input("enter"))
a=num%10
if a>0:
    print(a,"yes")
else:
    print(a,"No")
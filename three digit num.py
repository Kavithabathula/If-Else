# 40. Write a program to check whether a number entered is a three digit number or not.

num=int(input("enter"))
if num>99 and num<1000:
    print(num,"is three digit number")
else:
    print(num,"is not a three digit number")
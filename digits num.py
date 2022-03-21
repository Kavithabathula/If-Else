# 66. The given number is of one digited or two digited or three digited or more than three digited.

num=int(input("enter the number"))
if num>=1 and num<=9:
    print(num,"is a one digit number")
elif num>=10 and num<=99:
    print(num,"is a two digit number")
elif num>=100 and num<=999:
    print(num,"is a three digit number")
elif num>=1000 and num<=9999:
    print(num,"is a four digit number")
else:
    print(num)
# 2. Write a python program to find maximum between three numbers.

num1=int(input("enter"))
num2=int(input("enter"))
num3=int(input("enter"))
if num1>num2 and num1>num3:
    print("num1 is greater",num1)
elif num2>num1 and num2>num3:
    print("num2 is greater",num2)
else:
    print("num3 is greater",num3)
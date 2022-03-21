# 61.Write a Python program to test whether a number is within 100 of 1000 or 2000

a=int(input("enter"))
b=int(input("enter"))
n=100
if (n-1000)<=100:
    print("Correct")
elif (n-2000)<=100:
    print("Yes")
else:
    print("Incorrect")
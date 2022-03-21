# 14. Write a python program to input angles of a triangle and check whether triangle is valid or not.

a=int(input("enter"))
b=int(input("enter"))
c=int(input("enter"))
if a+b+c==180:
    print("Triangle")
else:
    print("not a triangle")
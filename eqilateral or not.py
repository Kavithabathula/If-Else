# 16. Write a python program to check whether the triangle is equilateral, isosceles or scalene triangle.

a=int(input("enter"))
b=int(input("enter"))
c=int(input("enter"))
if a==b and b==c:
    print("Equilateral")
elif a==b or b==c:
    print("Isoscale")
else:
    print("Scalene")
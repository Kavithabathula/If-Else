# 24. Take the age of 3 people by user and determine oldest and youngest among them.

age1=int(input("enter"))
age2=int(input("enter"))
age3=int(input("enter"))
if age1>age2 and age1>age3:
    print("age1 is oldest")
elif age2>age3 and age2>age1:
    print("age2 is oldest")
else:
    print("age3 is oldest")

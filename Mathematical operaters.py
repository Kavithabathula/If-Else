# 42. Write a program to accept two numbers and mathematical operators and perform operation accordingly.
# Like:
# Enter First Number: 7
# Enter Second Number : 9
# Enter operator : +
# Your Answer is : 16

a=int(input("enter"))
b=input("enter the operator")
c=int(input("enter"))
if b=="+":
    print("Answer",a+c)
elif b=="-":
    print("Answer is",a-c)
elif b=="*":
    print("Answer is",a*c)
elif b=="%":
    print("Answer is",a%c)
elif b=="//":
    print("Answer is",a//c)
elif b=="/":
    print("Answer is",a/c)
else:
    print("wrong")
# 63. Take 2 inputs and add them if the result is odd print result odd hain, and if it is not print odd nahi hain.

a=int(input("Enter the number"))
b=int(input("enter the number"))
sum=a+b
if sum%2!=0:
    print(sum,"Odd hain")
else:
    print(sum,"Odd nahi hain")
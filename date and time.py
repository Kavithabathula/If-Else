# 54. Write a Python program to display the current date and time.

# Sample Output :
# Current date and time
# 2014-07-05 14:34:14

year=int(input("enter"))
month=int(input("enter"))
date=int(input("enter"))
if date>=1 and date<=31 or month>=1 and month<=12:
    print(date,"/",month,"/",year)
else:
    print("Incorrect")
# 49.Write a Python program to get the next day of a given date.

# Expected Output:
# Input a year: 2016
# Input a month [1-12]: 08
# Input a day [1-31]: 23
# The next date is [yyyy-mm-dd] 2016-8-24


date=int(input("enter"))
month=int(input("enter"))
year=int(input("enter"))
if date>=1 and date<=31:
    print(date)
    if month>=1 and month<=12:
        print(month)
        if year>=1900 and year<=2100:
            print(year)
            print(date+1,"/",month,"/",year)
        else:
            print("wrong")
    else:
        print("Not correct")
else:
    print("Not right")
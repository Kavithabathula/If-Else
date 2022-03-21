# 12. Write a python program to input the month number and print the number of days in that month.


num=input("enter the number")
if num=="feb":
    print("28 or 29 days")
elif num=="apr" or "june" or "sep" or "nov":
    print("30 days")
else:
    print("31 days")
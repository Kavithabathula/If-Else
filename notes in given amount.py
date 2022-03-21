# 13. Write a python program to count the total number of notes in a given amount.

x=int(input("enter"))
if x>=10:
    print("10 notes",x//10)
if x>=30:
    print("30 notes",x//30)
if x>=60:
    print("60 notes",x//60)
if x>=100:
    print("100 notes",x//100)
if x>=300:
    print("300 notes",x//300)
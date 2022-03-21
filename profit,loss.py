# 17. Write a python program to calculate profit or loss.

selling=int(input("enter"))
cost=int(input("enter"))
amount=selling-cost
if amount>=cost:
    print("Profit")
else:
    print("Loss")
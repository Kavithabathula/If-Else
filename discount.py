# 21. A shop will give a discount of 10% if the cost of the purchased quantity is more than 1000. Ask the user
# for quantity, Suppose, one unit will cost 100. Judge and print total cost for user.


cost=int(input("enter"))
user=int(input("enter"))
total=cost*user*10/100
if total>100:
    print("Gives discount")
else:
    print("Not gives discount")
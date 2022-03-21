# 35. Write a program to accept the cost price of a bike and display the road tax to be paid according to the
# following criteria :
# a. Cost price (in Rs) Tax
# b. > 100000 15 %
# c. > 50000 and <= 100000 10%
# d. <= 50000 5%

cost=int(input("enter"))
tax=cost*int(input("enter"))/100
if cost>100000 and tax==tax:
    print("cost",tax)
elif cost>50000 and cost<100000:
    print("cost",tax)
elif cost<=50000 and tax==tax:
    print("cost",tax)
else:
    print("Not at all")
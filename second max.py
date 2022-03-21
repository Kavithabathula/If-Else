# num=int(input("enter"))
# b=len(num)-2
# c=int(num)//10**b
# d=10%c
# if d==3:
#     print("Yes")
# else:
#     print("No")



num=int(input("enter"))
if (num//100)%10==3:
    print("Yes")
else:
    print("No")
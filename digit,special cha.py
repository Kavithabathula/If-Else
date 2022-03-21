# 9. Write a python program to input any character and check whether it is alphabet, digit or special
# character.

upper=input("enter")
if upper>="A" and upper<="Z":
    print(upper)
    lower=input("enter")
    if lower>="a" and lower<="z":
        print(lower)
        sc=input("enter")
        if sc>="@" and sc<="#":
            print(sc)
            digit=int(input("enter"))
            if digit>=1 and digit<=9:
                print(digit)
            else:
                print("No")
        else:
            print("Wrong")
    else:
        print("Not")
else:
    print("Not correct")
alp=input("enter")
sc=input("enter")
num=int(input("enter"))
if alp>="a" and alp<="z" or alp>="A" and alp<="Z":
    print("alphabet")
    # sc=input("enter")
    if sc>="@" or sc<="#":
        print("special character")
        # num=int(input("enter"))
        # if num>=1 and num<=100:
        if num:
            print("number")
            if alp>="a" and alp<="z" and sc and num:
                print(alp+sc+str(num))
            else:
                print("wrong")
        else:
            print("wrong")
    else:
        print("wrong")
else:
    print("wrong")
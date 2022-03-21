insta=input("enter")
if insta==insta:
    print("open Instagram")
    name=input("enter the upper case")
    if name>="A" and name<="Z":
        print(name)
        small=input("enter lower case")
        if small>="a" and small<="z":
            print(small)
            num=int(input("enter"))
            # if num>="1" and num<="9":
            if num:
                print(str(num))
                print("Now start your videos")
                print("Add your friends")
                print("Say hi to you friends")
            else:
                print("wrong")
        else:
            print("wrong")
    else:
        print("wrong")
else:
    print("wrong")
Gmail=input("Create an account")
name=input("Enter the name")
if name>="a" and name<="z":
    print("okay")
    user=input("Enter the user name")
    if user>="a" and user<="z" or user>="A" and user<="Z":
        print(user)
        sc=input("Enter the special charecter")
        if sc>="@" and sc<="#":
            print(sc)
            num=int(input("Enter the value"))
            if num:
                print(str(num))
                pw=input("Enter the password")
                alp=input("Enter the alphabet")
                sc=input("Enter the special character")
                num=int(input("enter"))
                if alp>="a" and alp<="z":
                    print(alp)
                    if sc>="@" and sc<="#":
                        print(sc)
                        if num:
                            print(str(num))
                            if alp>="a" and alp<="z"and sc and num:
                                print(alp+sc+str(num))
                                birth=input("Enter the date")
                                if "day/month/year":
                                    print(birth)
                                    gender=input("Enter the gender")
                                    if gender=="female" and gender=="male":
                                        print(gender)
                                        print("I Agree")
                                        print("Okay")
                                        print("Click on next")
                                        print("Yess,I am in")
                                    else:
                                        print("wrong")
                                else:
                                    print("wrong")
                            else:
                                print("wrong")
                        else:
                            print("wrong")
                    else:
                        print("wrong")
                else:
                    print("wrong")
            else:
                print("wrong")
        else:
            print("wrong")
    else:
        print("wrong")
else:
    print("wrong")
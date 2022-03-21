open=input("open Facebook app")
print("App opened")
new=input("Create new accoount")
if "new==new":
    print("Created facebbok")
    name=input("enter the name")
    if name>="a" and name<="z":
        print(name)
        sur=input("enter the surname")
        if sur>="a" and sur<="z":
            print(sur)
            birth=int(input("enter"))
            if "date/month/year":
                print(birth)
                gender=input("enter the gender")
                if gender=="female" or gender=="male":
                    print(gender)
                    pw=input("enter the password")
                    if pw>="a" and pw<="z":
                        print(pw)
                        print("enter the OTP")
                        print("Now you are in Facebook")
                    else:
                        print("Wrong")
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
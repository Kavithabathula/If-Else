ATM="Please enter the ATM card"
print("Please insert the card")
if "ATM"=="ATM":
    print("Next")
    lan=input("Select your language")
    if lan=="english" or lan=="hindi" or lan=="telugu":
        print(lan)
        num=int(input("enter the number between 10-99"))
        if num:
            print("33")
            pin=int(input)("enter the number")
            if num:
                print("okay next")
                select=input("select transaction")
                if select=="withdrawl" or select=="checking amount":
                    print(select)
                    save=input("from current account")
                    if save=="current amount":
                        print("From savings")
                        amount=int(input("enter the amount"))
                        if amount=="10000":
                            print("It is in processing")
                            print("Collect your cash")
                            print("Take your ATM card")
                            print("Thank you")
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
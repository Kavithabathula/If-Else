num=int(input("enter"))
if num>0:
    n=num%10
    digit=num//10
    print(n)
    if digit>0:
        n1=digit%10
        digit1=digit//10
        print(n1)
        if digit>0:
            n2=digit1%10
            print(n2)
            print(n,n1,n2)
    else:
            print("wrong")
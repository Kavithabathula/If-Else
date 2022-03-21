# 20. Write a python program to input electricity unit charges and calculate total electricity bill according to the
# given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill


charges=int(input("enter"))
unit=int(input("enter"))
total=charges*unit*20/100
if charges<50:
    print("low")
elif charges>50 and charges<100:
    print("medium")
elif charges>100 and charges<200:
    print("little")
elif charges<250:
    print("higher")
else:
    print("not valid")
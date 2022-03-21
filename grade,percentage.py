# 18. Write a python program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and
# Computer. Calculate percentage and grade according to following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F


phy=int(input("enter"))
chem=int(input("enter"))
bio=int(input("enter"))
math=int(input("enter"))
com=int(input("enter"))
total=phy+chem+bio+math+com
per=total/100*500
if per>=90:
    print("Grade A")
elif per>=80:
    print("Grade B")
elif per>=70:
    print("Grade C")
elif per>=60:
    print("Grade D")
else:
    print("Fail")
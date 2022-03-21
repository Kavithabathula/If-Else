# 25. A student will not be allowed to sit in an exam if his/her attendance is less than 75%.Take following
# input from the user. Number of classes held. Number of classes attended. And print, percentage of
# class attended. Is the student is allowed to sit in the exam or not.

class_held=int(input("enter"))
class_attended=int(input("enter"))
if class_attended>=75:
    print("Allowed to Exam")
else:
    print("Not allowed to Exam")
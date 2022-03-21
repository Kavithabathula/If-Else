# 47. Write a Python program that reads two integers representing a month and day and prints the season
# for that month and day.
# a. Expected Output:
# Input the month (e.g. January, February etc.): july
# Input the day: 31
# Season is autumn

season=input("enter")
if season=="jan" or "feb" or "mar" or "apr":
    print("Winter season")
elif season=="may" or "june" or "july" or "aug":
    print("Summer season")
else:
    print("Rainy season")
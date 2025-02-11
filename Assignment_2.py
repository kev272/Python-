#1.A program to check if a month is a leap month or not
from calendar import month

month = int(input("enter numbers of days in the month: "))
if month == 29 :
    print("leap year")
elif month == 28 :
    print(" not leap year")
else :
    print("invalid input")

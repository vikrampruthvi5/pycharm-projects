
import time
from datetime import date

# name = input("Enter your name : ")
# age = int(input("Enter your age : "))
# repeat = int(input("How many time you want to repeat the message : "))
name = "Vikram"
age = 25
repeat = 2
year = date.today().year

turns_100 = 100-age
turns_100_year = year+turns_100

if age > 100:
    print(name, "is already 100 years old")
    exit(0)
elif age is 100:
    print(name, "just turned 100")
    exit(0)
else:
    for i in range(repeat):
        print(name, "will turn 100 in the year", turns_100_year)
        exit(0)
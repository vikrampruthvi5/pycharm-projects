# IF ELSE IF

'''
Write a program to define person's category from person's age
'''

pDef = ""
age: int = 0

name = input("Enter the name: ")
age = int(input("Enter {0}'s age: ".format(name)))

# name = 'Vikram'
# age = 25

if age > 0:
    if age < 21 and age > 12:
        pDef = "Young"
    elif age > 21 & age < 45:
        pDef = "Adult"
    else:
        pDef = "Old"

else:
    print("0 is invalid or age not entered")
    exit(0)

print("\n", name, "is", age, "years old and falls under", pDef, "category")

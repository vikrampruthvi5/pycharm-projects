
"""
Variable scope

If you declare a variable in a function, only that function can use the variable.
Its scope is defined to that particular function

If its declared outside the function that is called global declaration and all the functions
in that program can use the variable.

"""
b = 30


def printA():
    a = 20
    print(a)

def printB():
    try:
        print(a) # This will not be printed as the scope of a is only till function printA()
    except:
        print("variable not found")

    print(b)


printA()
printB()





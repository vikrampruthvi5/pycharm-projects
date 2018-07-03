"""

Issue : Until now we know how many args are required for a function
        But if we dont know the total number of arguments we donno what
        to do

Solution:   use method where we can pass * in the arguments which makes unlimited arguments

"""

def add_numbers(*args): # Here args is just a name of variable. Not a keyword
    tot_str = ""
    total = 0
    for a in args:

        total = total + a
    print("No. of arguments = ",len(args))
    print(total)


add_numbers(3)
add_numbers(3, 2, 5)
add_numbers(21, 23, 52344, 123, 54)

def allowed_dating_age(my_age):
    girls_age = my_age/2+7
    return girls_age


date_limit = allowed_dating_age(float(input("Enter your age : ")))
print("You can date girls with age", date_limit, "or older")


"""
Functions can return values of for a processed data. 
You can store the value and reuse it.
RETURN keyword helps you to do that.
"""
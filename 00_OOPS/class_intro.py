"""
For code re usability we are going to use classes.
Classes makes programming easy as you dont have to write again and again

Ex : Imagine that you are a owner of a company and decided to store employees data
 1. You can create 1 Employee class and create as many instances as required.
"""


class Employee:

    # This is the constructor in Python
    #   A constructor is a function that is invoked automatically
    #    by creating instance for a class
    def __init__(self, first: str, last: str, salary: int):
        self.first = first
        self.last = last
        self.salary = salary

    @classmethod
    def obj_from_string(cls, string: str):
        first, last, sal = string.strip().split('-')
        return cls(first, last, int(sal))

    def print_details(self):
        return "{} {} {}".format(self.first, self.last, self.salary)


e1 = Employee("Pruthvi", "Vikram", 70000)
print(e1.print_details())

print(Employee.print_details(e1))

string1 = "Samyuktha-Dukkipati-75000"
string2 = "Srinivasa rao-Vikram-100000"

e2 = Employee.obj_from_string(string1)
e3 = Employee.obj_from_string(string2)

print(e2.print_details() + "\n" + e3.print_details())




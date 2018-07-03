
"""

Previously we have seen how to pass values as arguments to the parameters of the function

In this example we will see how to send only few values to only one parameters

"""
from dbm import dumb


def dumb_sentence(name='Vikram', action='ate', item='Tuna'):
    print(name, action, item)


dumb_sentence()
dumb_sentence('Sampath', 'played', 'TT')

# Here we are going to send only one parameter value instead of all
dumb_sentence(item='Chicken')
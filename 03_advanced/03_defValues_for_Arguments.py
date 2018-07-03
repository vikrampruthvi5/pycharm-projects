
"""
Default values for arguments...

You can have extra variables/extra information. This is also called as arguments.
ex: def get_gender(sex='unknown') # Here we are passing default value as argument

"""


def get_gender(sex='unknown'):
    if sex is 'm':
        sex = 'Male'
    if sex is 'f':
        sex = 'Femaale'
    print(sex)

get_gender('m')
get_gender('f')
get_gender()

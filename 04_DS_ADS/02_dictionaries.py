"""
Dictionaries : Just like the name says, KEY VALUE pairs exists
"""


friends = {
    'samyuktha' :   'My wife',
    'Badulla'   :   'I hate him',
    'Sampath'   :   'Geek I like'
}

for k, v in friends.items(): # This can be used to iterate through the dictionary and print keys, values
    print(k ,v)


"""
Trying dictionaries as values for a dictionary
Template:
    'brand' : {
        'model' :   "",
        'year'  :   YYYY,
        'miles' :   xxxxx.xx,
        'owner' :   ""
    },

"""
cars = {
    'Honda' : [
        {
        'model' :   "Accord",
        'year'  :   2018,
        'miles' :   30685.34,
        'owner' :   "Pruthvi"
        },
        {
        'model' :   "Accord",
        'year'  :   2018,
        'miles' :   30685.34,
        'owner' :   "Pruthvi"
        }
    ],
    'Toyota' : [{
        'model' :   "Altis",
        'year'  :   2013,
        'miles' :   3068.34,
        'owner' :   "Samyuktha"
    }]
}

#Above : Each mode will have multiple cars
for k, v in cars.items():
    print(k, v[0])
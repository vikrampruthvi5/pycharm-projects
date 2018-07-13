
"""
    Target of this program is to experiment with urllib.request library and understand GET and POST methods
    Tasks:
    1. Create json server locally
    2. retrieve json file using url
    3. process json data and perform some actions
    4. Try POST method
"""

"""
   1. Create json server locally
    a. From terminal
        install json-server : sudo npm install -g json-server
        create a folder or file with json data ex: people.json
    b. Start observing the json file
        json-server --watch people.json
    c. Make sure you are getting 
        Resources
        http://localhost:3000/people

        Home
        http://localhost:3000
"""


"""
    2. retrieve json file using url
"""

import urllib.request as req
import json

def get_json_data(url):
    # Method to retrieve json data
    data = req.urlopen(url)
    data_json = json.loads(data.read())
    return data_json

def post_json_data(url):
    # Method posts json data to the json file under server
    print("Post method")

def print_json_data(json):
    for i in range(len(json)):
        print(json[i]['name'],"is",json[i]['age'],"years old.")


json = get_json_data("http://localhost:3000/people")
print_json_data(json)


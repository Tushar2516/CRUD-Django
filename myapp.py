import json
import requests

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None): # check Id 
    data = {}
    if id is not None:  # if ID is Their
        data = {'id': id}  #run 
    json_data = json.dumps(data)  # convert requested data python  into JSON 
    r = requests.get( url = URL, data = json_data) # request send to URL.py and URL.py transfer link to View.py 
    data = r.json() # get data from backend
    print(data)

# get_data()    # Function Call with Argument If You Want


def post_data():
    data = { 
        'name': 'chetan',
        'roll': 108,
        'city' : 'surat'
    }
    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)

post_data()

def update_data():
    data = { 
        'id': 1,
        'name': 'GaTu',
        # 'roll': 107,
        'city' : 'Dalal Street'
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)

# update_data()

def delete_data():
    data = { 
        'id': 6
    }
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)

# delete_data()  
# in this we are getting data i.e taking data from url
import requests
import json

URL = "http://127.0.0.1:8000/api_view"


# we are fetching data on basis of id if no id is given than give complete data


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.get(url=URL, headers=headers,data=json_data)

    # after getting data we get that data in r varaible hence to fetch that data we use json

    data = r.json()
    print(data)


# if id is not given than gives complete data..


# a = int(input("Enter the id:"))
# get_data(id=a)


# get_data()


# for passing data here and creating it in database

def post_data():
    data = {
        'name': "Gohit",
        'roll': 104,
        'city': "dham",

    }
#without below u will get error that content type is not defined to solve this u need to add below codde

    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.post(url=URL,headers=headers, data=json_data)

    data = r.json()
    print(data)


# post_data()
# u can ucomment to do stuf


# for updating the data
def update_data():
    data = {
        'id': 4,
        'name': "Rohan",
        'city': "USA",

    }
    

    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.put(url=URL,headers=headers,data=json_data)

    # after getting data we get that data in r varaible hence to fetch that data we use json

    data = r.json()
    print(data)

# update_data()


# for deletting th data
def delete_data():
    data = {'id': 1}
# above data currently is in dict form and we need to share it in json format

    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.delete(url=URL ,headers=headers, data=json_data)

    # after getting data we get that data in r varaible hence to fetch that data we use json

    data = r.json()
    print(data)

delete_data()

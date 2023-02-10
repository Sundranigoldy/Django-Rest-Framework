# in this we are getting data i.e taking data from url
import requests
import json

URL = "http://127.0.0.1:8000/read"

# we are fetching data on basis of id if no id is given than give complete data


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    # taking data 1st converting to json and using get taking data
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)

    # after getting data we get that data in r varaible hence to fetch that data we use json

    data = r.json()
    print(data)


# if id is not given than gives complete data..


# a = int(input("Enter the id:"))
# get_data(id=a)


# get_data()
# if u want to read data just uncomment above


# for passing data here and creating it in database

def post_data():
    data = {
        'name': "Gohit",
        'roll': 123,
        'city': "dham",

    }
# above data currently is in dict form and we need to share it in json format

    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)

    # after getting data we get that data in r varaible hence to fetch that data we use json

    data = r.json()
    print(data)


post_data()
# u can ucomment to do stuf


# for updating the data
def update_data():
    data = {
        'id': 5,
        'name': "Goldy",
        'city': "USA",

    }
# above data currently is in dict form and we need to share it in json format

    json_data = json.dumps(data)
    # for updating we use put request
    r = requests.put(url=URL, data=json_data)

    # after getting data we get that data in r varaible hence to fetch that data we use json

    data = r.json()
    print(data)

# update_data()


# for deletting th data
def delete_data():
    data = {'id': 2}
# above data currently is in dict form and we need to share it in json format

    json_data = json.dumps(data)
    # for updating we use put request
    r = requests.delete(url=URL, data=json_data)

    # after getting data we get that data in r varaible hence to fetch that data we use json

    data = r.json()
    print(data)

# delete_data()

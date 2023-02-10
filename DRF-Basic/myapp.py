import requests

#adding url
URL = "http://127.0.0.1:8000/"

# in our get request
r = requests.get(url=URL)
# converting data into json
data = r.json()
#printing data
print(data)
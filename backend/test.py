import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "posts") #get request to BASE + given url
print(response.json())




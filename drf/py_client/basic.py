import requests

endpoint = 'http://127.0.0.1:8000/api/'

response = requests.post(endpoint ,json= {"title":"None111", 'price': 12/3 ,"content":"This is content"}, )
print(response.json())
# print(response.json()['message'])

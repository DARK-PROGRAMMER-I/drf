import requests

endpoint = 'http://127.0.0.1:8000/api/products/8/'

response = requests.get(endpoint )
print(response.json())
# print(response.json()['message'])

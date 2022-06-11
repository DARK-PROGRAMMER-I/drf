import requests

endpoint = 'http://127.0.0.1:8000/api/'

response = requests.get(endpoint, params={'product_id':123} ,json= {"query":"Hellow world"})
print(response.json())
# print(response.json()['message'])

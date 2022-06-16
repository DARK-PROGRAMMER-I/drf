import requests

endpoint = 'http://127.0.0.1:8000/api/products/8/update/'
data = {
    'title': 'Again Updated 8',
}
response = requests.put(endpoint, json=data )
print(response.json())
# print(response.json()['message'])

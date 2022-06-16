import requests
product_id = int(input('What product you want to delete? Enter id: '))

if product_id:
    endpoint = f'http://127.0.0.1:8000/api/products/{product_id}/delete/'

    response = requests.delete(endpoint)
    # print(response.status_code,response.status_code == 204 )
    if response.status_code == 204:
        print('Product Deleted! ')
    else:
        print('No matching product for this id')
    # print(response.json()['message'])
else:
    print('This product is not available')

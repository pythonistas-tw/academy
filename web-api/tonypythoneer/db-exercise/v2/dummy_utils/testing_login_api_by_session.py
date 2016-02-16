import requests
import json

headers = {
    'content-type': 'application/json'
}
data = {
    "email": "123@123.com",
    "password": "123"
}
res = requests.post('http://192.168.2.165:5000/users/login', data=json.dumps(data), headers=headers)


r = requests.get('http://192.168.2.165:5000/users/1', cookies=dict(res.cookies))

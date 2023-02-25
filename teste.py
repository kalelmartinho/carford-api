import requests

payload = {
    'name': 'Jack',
    'phone': '41987425031',
    'email': 'jack@gmail.com'
}

car_payload = {
    'owner_id': 1,
    'model': 'hatch',
    'color': 'yellow'
}

#r = requests.post('http://localhost:5000/car', json=car_payload)
r = requests.post('http://localhost:5000/owner', json=payload)

print(r.text)
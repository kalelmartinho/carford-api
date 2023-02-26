from app.models.car import Car


def test_get_cars_by_owner_id(test_client):
    client, token = test_client
    response = client.get('/api/cars/1', headers={'Authorization': f'Bearer {token}'})

    assert response.status_code == 200



def test_add_car(test_client):
    client, token = test_client
    data = {
        'owner_id': 1,
        'model': 'sedan',
        'color': 'blue'

    }
    response = client.post('/api/cars', json=data, headers={'Authorization': f'Bearer {token}'}, follow_redirects=True)

    assert response.status_code == 201
    assert response.json['car']['model'] == 'sedan'
    assert response.json['car']['color'] == 'blue'


def test_update_car(test_client):
    client, token = test_client
    data = {
        'model': 'hatch',
        'color': 'yellow',
        'owner_id': 1
    }
    response = client.put('/api/cars/1', json=data, headers={'Authorization': f'Bearer {token}'})

    assert response.status_code == 200
    assert response.json['car']['model'] == 'hatch'
    assert response.json['car']['color'] == 'yellow'

def test_add_car_max_limit(test_client):
    client, token = test_client
    data = {
    'owner_id': 1,
    'model': 'hatch',
    'color': 'yellow'
    }
    # adding more cars to the owner with id=1
    response = client.post('/api/cars', json=data, headers={'Authorization': f'Bearer {token}'}, follow_redirects=True)
    assert response.status_code == 400
    assert response.json['error'] == 'Owner John Doe already has the maximum number of cars (3)'

def test_add_car_with_invalid_data(test_client):
    client, token = test_client
    data = {
        'owner_id': 1,
        'model': 'invalid_model',
        'color': 'invalid_color'

    }
    response = client.post('/api/cars', json=data, headers={'Authorization': f'Bearer {token}'}, follow_redirects=True)

    assert response.status_code == 400
    assert 'error' in response.json

def test_delete_car(test_client):
    client, token = test_client
    response = client.delete('/api/cars/1', headers={'Authorization': f'Bearer {token}'})

    assert response.status_code == 204
    assert Car.query.get(1) is None



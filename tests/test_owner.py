from app.models.owner import Owner


def test_get_owner(test_client):
    client, token = test_client
    response = client.get('/api/owners/1', headers={'Authorization': f'Bearer {token}'})

    assert response.status_code == 200
    assert response.json['name'] == 'John Doe'


def test_add_owner(test_client):
    client, token = test_client
    data = {
        'name': 'Jane Smith',
    }
    response = client.post('/api/owners', headers={'Authorization': f'Bearer {token}'}, json=data, follow_redirects=True)

    assert response.status_code == 201
    assert response.json['name'] == 'Jane Smith'


def test_update_owner(test_client):
    client, token = test_client
    data = {
        'name': 'Janete Doe',
    }
    response = client.put('/api/owners/1', headers={'Authorization': f'Bearer {token}'}, json=data)

    assert response.status_code == 200
    assert response.json['name'] == 'Janete Doe'


def test_delete_owner(test_client):
    client, token = test_client
    response = client.delete('/api/owners/1', headers={'Authorization': f'Bearer {token}'})

    assert response.status_code == 204
    assert Owner.query.get(1) is None
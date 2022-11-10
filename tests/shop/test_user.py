import pytest


@pytest.mark.django_db
def test_register_user(client):
    payload = dict(
        username="mohh",
        password="test54321"
    )

    response = client.post('/register/', payload)

    data = response.data

    assert data['username'] == payload['username']
    assert "password" not in data


@pytest.mark.django_db
def test_login_user(user, client):
    response = client.post(
        '/api-token-auth/', dict(username="mohh", password="test4321"))

    assert response.status_code == 200


@pytest.mark.django_db
def test_login_user_fail(client):
    payload = dict(
        username="bob",
        password="test54321"
    )

    response = client.post('/api-token-auth/', payload)
    assert response.status_code == 400

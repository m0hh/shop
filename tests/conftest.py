import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.fixture
def user():
    user = User(
        username="mohh",
    )
    user.set_password("test4321")
    user.save()
    return user


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def token(client, user):
    response = client.post(
        '/api-token-auth/', dict(username="mohh", password="test4321"))
    return response.data['token']

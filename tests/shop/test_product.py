import pytest
from product import models


@pytest.mark.django_db
def test_create_product(token, client, user):
    payload = dict(
        name="product1",
        price=20
    )

    response = client.post('/product/create/', payload,
                           HTTP_AUTHORIZATION=f'Token {token}')

    data = response.data
    product_from_db = models.Product.objects.all().first()

    assert data['name'] == product_from_db.name
    assert data['id'] == product_from_db.id
    assert data['price'] == product_from_db.price
    assert data['owner'] == user.id


@pytest.mark.django_db
def test_get_product(client, user):
    models.Product.objects.create(name="product1", price=20, owner=user)
    models.Product.objects.create(name="product2", price=20, owner=user)

    response = client.get('/product/list')

    assert response.status_code == 200
    assert len(response.data) == 2

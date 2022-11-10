import pytest
from product.models import Product
from cart.models import Cart


@pytest.mark.django_db
def test_create_order(user, token, client):
    product1 = Product.objects.create(name="Product 1", price=20, owner=user)
    product2 = Product.objects.create(name="Product 2", price=30, owner=user)
    cart = Cart.objects.create(owner=user)
    cart.products.add(product1)
    cart.products.add(product2)

    response = client.post(
        '/order/create/', HTTP_AUTHORIZATION=f"Token {token}")

    assert len(response.data) == 2

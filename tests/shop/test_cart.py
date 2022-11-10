import pytest
from product.models import Product
from cart.models import Cart


@pytest.mark.django_db
def test_cart_add(user, client, token):
    product = Product(name="product1", price=20, owner=user)
    product.save()
    payload = dict(
        product=product.id
    )
    response = client.post('/cart/add/', payload,
                           HTTP_AUTHORIZATION=f'Token {token}')
    cart_from_db = Cart.objects.get(owner=user)

    assert response.data['products'] == list(
        cart_from_db.products.values_list('id', flat=True))
    assert response.data['owner'] == user.id
    assert response.data['id'] == cart_from_db.id

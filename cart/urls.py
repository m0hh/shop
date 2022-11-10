from django.urls import path
from cart.views import AddToCart, RemoveFromCart, GetCart
urlpatterns = [
    path('add/', AddToCart.as_view(), name="addtocart"),
    path('remove/', RemoveFromCart.as_view(), name="removefromcart"),
    path('get/', GetCart.as_view(), name="getcart")


]

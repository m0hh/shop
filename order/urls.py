from django.urls import path
from order.views import CreateOrder, GetOrders
urlpatterns = [
    path('create/', CreateOrder.as_view(), name="createorder"),
    path('get/', GetOrders.as_view(), name="getorder")
]

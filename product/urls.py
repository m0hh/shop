from django.urls import path
from product.views import ProductCreate, ProductList

urlpatterns = [
    path('create/', ProductCreate.as_view(), name="createproduct"),
    path('list', ProductList.as_view(), name="listproduct")

]

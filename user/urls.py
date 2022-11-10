from django.urls import path
from user.views import UserReg
from rest_framework.authtoken import views


urlpatterns = [
    path('register/', UserReg.as_view(), name='register'),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),

]

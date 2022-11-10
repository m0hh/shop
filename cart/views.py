from rest_framework.views import APIView
from rest_framework import authentication, permissions
from cart.models import Cart
from rest_framework.response import Response
from cart.serializer import CartSerializer
from rest_framework import status
from product.models import Product


class AddToCart(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        if "product" in request.data and Product.objects.filter(pk=request.data['product']).exists():
            cart, _ = Cart.objects.get_or_create(owner=self.request.user)
            cart.products.add(request.data['product'])
            serializer = CartSerializer(cart)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"messgae": "You need to send a product Id to be added to cart or you sent a wrong product Id"}, status=status.HTTP_400_BAD_REQUEST)


class RemoveFromCart(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        if "product" in request.data:
            cart, _ = Cart.objects.get_or_create(owner=self.request.user)

            if request.data['product'] not in list(cart.products.values_list('id', flat=True)):
                return Response({"messgae": "no product in the cart by that id"}, status=status.HTTP_400_BAD_REQUEST)
            cart.products.remove(request.data['product'])
            serializer = CartSerializer(cart)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"messgae": "You need to send a product Id to be added to cart"}, status=status.HTTP_400_BAD_REQUEST)


class GetCart(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        cart, _ = Cart.objects.get_or_create(owner=self.request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)

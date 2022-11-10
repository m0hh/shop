from rest_framework.views import APIView
from rest_framework import authentication, permissions
from cart.models import Cart
from order.models import Order
from rest_framework.response import Response
from rest_framework import status
from order.serializers import OrderSerializer


class CreateOrder(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        try:
            cart = Cart.objects.get(owner=request.user)
            orders = []
            if cart.products.all().count() > 0:
                for product in cart.products.all():
                    order = Order(owner=request.user, product=product)
                    order.save()
                    orders.append(order)
                cart.products.clear()
                serializer = OrderSerializer(orders, many=True)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "cart is empty"}, status=status.HTTP_400_BAD_REQUEST)
        except Cart.DoesNotExist:
            return Response({"message": "cart is empty"}, status=status.HTTP_400_BAD_REQUEST)


class GetOrders(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(owner=request.user)
        if orders.count() > 0:
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "no orders"}, status=status.HTTP_404_NOT_FOUND)

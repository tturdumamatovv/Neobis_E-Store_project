from rest_framework import generics, viewsets, response
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import permissions, views
from django.db.models import Avg
from rest_framework.viewsets import ModelViewSet

from .permission import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .models import *
from .serializers import *


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return ProductListDetailSerializer

    # api/v1/products/<id>/reviews/
    @action(['GET', 'POST'], detail=True)
    def reviews(self, request, pk=None):
        product = self.get_object()
        if request.method == 'GET':
            reviews = product.reviews.all()
            serializer = ReviewSerializer(reviews, many=True).data
            return response.Response(serializer, status=200)
        data = request.data
        serializer = ReviewSerializer(data=data, context={'request': request, 'product': product})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=201)


class CreateOrderView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserOrderList(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        orders = user.orders.all()
        serializer = OrderSerializer(orders, many=True).data
        return response.Response(serializer, status=200)


class UpdateOrderStatusView(views.APIView):
    permission_classes = (permissions.IsAdminUser,)

    def patch(self, request, pk):
        status = request.data['status']
        if status not in ['in_process', 'closed']:
            return response.Response('Invalid Status', status=400)
        order = Order.objects.get(pk=pk)
        order.status = status
        order.save()
        serializer = OrderSerializer(order).data
        return response.Response(serializer, status=206)



# class ProductAPIList(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly, )
#
#
# class ProductAPIUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = (IsOwnerOrReadOnly, )
#
#
# class ProductAPIDestroy(generics.RetrieveDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = (IsOwnerOrReadOnly, )

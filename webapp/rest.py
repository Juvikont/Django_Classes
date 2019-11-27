from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from .models import *
from rest_framework.pagination import LimitOffsetPagination


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    pagination_class = LimitOffsetPagination


class CartSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class CartViewSet(ModelViewSet):
    queryset = CartItem.objects.all().order_by('id')
    serializer_class = CartSerializer

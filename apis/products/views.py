from rest_framework import generics
from rest_framework.permissions import AllowAny

from apis.products.serializers import ProductListSerializer, ProductSerializer
from products.models import Product


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.prefetch_related('categories').all()
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]


class ProductView(generics.RetrieveAPIView):
    queryset = Product.objects.prefetch_related('categories').all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

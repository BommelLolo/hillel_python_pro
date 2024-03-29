# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
# from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny

# from apis.products.paginators import ProductPaginator
from apis.products.serializers import ProductListSerializer, \
    ProductDetailSerializer, ProductDeleteSerializer, \
    ProductCreateSerializer, ProductSerializer
from products.models import Product


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.prefetch_related('categories').all()
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.prefetch_related('categories').all()
    serializer_class = ProductDetailSerializer
    permission_classes = [AllowAny]


class ProductDelete(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDeleteSerializer
    permission_classes = [AllowAny]

    def perform_destroy(self, instance):
        serializer = self.get_serializer(instance, data={})
        serializer.is_valid(raise_exception=True)
        instance.delete()


class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [AllowAny]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = IsAuthenticated
    # pagination_class = ProductPaginator
    # filter_backends = (DjangoFilterBackend, SearchFilter)
    # search_fields = ['name']
    # filterset_fields = ('sku', 'is_active')

    def perform_destroy(self, instance):
        serializer = ProductDeleteSerializer(instance, data={})
        serializer.is_valid(raise_exception=True)
        instance.delete()

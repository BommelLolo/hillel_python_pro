# from django.urls import path
from rest_framework.routers import SimpleRouter

from apis.products.views import ProductViewSet
# ProductList, ProductDetail, ProductDelete, ProductCreate

# urlpatterns = [
#     path('products/', ProductList.as_view()),
#     path('products/create', ProductCreate.as_view()),
#     path('products/<uuid:pk>/detail', ProductDetail.as_view()),
#     path('products/<uuid:pk>/delete', ProductDelete.as_view()),
# ]

router = SimpleRouter()
router.register(r'products', ProductViewSet, basename='products')
urlpatterns = router.urls

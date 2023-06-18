from django.urls import path

from apis.products.views import ProductList, ProductView

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('<uuid:pk>', ProductView.as_view()),
]

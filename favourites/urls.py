from django.urls import path

from favourites.views import FavouriteProductList, \
    AddOrRemoveFavoriteProduct, AJAXAddOrRemoveFavoriteProduct

urlpatterns = [
    path('', FavouriteProductList.as_view(), name='favourites'),
    path('<uuid:pk>/', AddOrRemoveFavoriteProduct.as_view(),
         name='add_or_remove_favourite'),
    path('ajax/<uuid:pk>/', AJAXAddOrRemoveFavoriteProduct.as_view(),
         name='ajax_add_or_remove_favourite'),
]

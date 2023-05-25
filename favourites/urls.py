from django.urls import path

from favourites.views import FavouriteView

urlpatterns = [
    path('', FavouriteView.as_view(), name='favourites')
]

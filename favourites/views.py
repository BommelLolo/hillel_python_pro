from django.views.generic import ListView

from favourites.models import Favourite


class FavouriteView(ListView):
    template_name = 'favourites/index.html'
    model = Favourite

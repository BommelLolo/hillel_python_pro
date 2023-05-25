from django import forms

from favourites.models import Favourite


class FavouriteModelForm(forms.ModelForm):
    class Meta:
        model = Favourite
        fields = ('user', 'group', 'products')

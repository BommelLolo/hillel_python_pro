from django import forms

from orders.models import Order


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('order_number', 'user', 'total_amount', 'is_paid')

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].initial = user

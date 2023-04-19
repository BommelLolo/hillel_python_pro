from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import render

from orders.model_forms import OrderModelForm
from orders.models import Order


class OrderView(FormView):
    form_class = OrderModelForm
    template_name = 'orders/index.html'
    success_url = reverse_lazy('orders')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_context_data(self, **kwargs):
        kwargs['orders'] = Order.objects.iterator()
        context = super().get_context_data(**kwargs)
        context.update({'form': self.form_class})
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'orders/index.html', context={
            'order': Order.objects.iterator(),
            'form': form
        })

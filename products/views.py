from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import render

from products.model_forms import ProductModelForm
from products.models import Product


class ProductView(FormView):
    form_class = ProductModelForm
    template_name = 'products/index.html'
    success_url = reverse_lazy('products')

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'products/index.html', context={
            'products': Product.objects.iterator(),
            'form': form
        })

    def get_context_data(self, **kwargs):
        kwargs['products'] = Product.objects.iterator()
        context = super().get_context_data(**kwargs)
        context.update({'form': self.form_class})
        return context

# from django.shortcuts import render
# from products.model_forms import ProductModelForm
# from products.models import Product
#
#
# def products(request, *args, **kwargs):
#     # 3-rd variant forms. FOR USE
#     form = ProductModelForm
#     if request.method == 'POST':
#         form = form(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#     # else:
#     #     form = form()
#     return render(request, 'products/index.html', context={
#         'products': Product.objects.iterator(),
#         'form': form
#     })

from django.shortcuts import render

from products.forms import ProductModelForm
from products.models import Product


def products(request, *args, **kwargs):
    # 3-rd variant forms. FOR USE
    form = ProductModelForm
    if request.method == 'POST':
        form = form(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
    # else:
    #     form = form()
    return render(request, 'products/index.html', context={
        'products': Product.objects.iterator(),
        'form': form
    })

    # # 2-nd variant forms. Don't use it
    # form = ProductForm
    # if request.method == 'POST':
    #     form = form(data=request.POST, files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    # else:
    #     form = form()
    # products_list = Product.objects.iterator()
    # return render(request, 'products/index.html', context={
    #     'products': products_list,
    #     'form': form
    # })

    # # 1-st variant forms. Don't use it
    # if request.method == 'POST':
    #     form = ProductForm(data=request.POST, files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    # products_list = Product.objects.iterator()
    # return render(request, 'products/index.html', context={
    #     'products': products_list
    # })

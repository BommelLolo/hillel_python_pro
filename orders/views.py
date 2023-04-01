from django.shortcuts import render


def orders(request, *args, **kwargs):
    return render(request, 'orders/index.html')

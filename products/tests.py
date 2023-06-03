from django.urls import reverse
from random import randint

from products.models import Product


def test_products_list(client, product_factory, faker):
    for _ in range((randint(3, 20))):
        product_factory()
    url = reverse('products')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.context['products']) == Product.objects.count()

#
# def test_product_detail(client, product_factory, faker):
#     product_factory()
#     url = reverse('products')
#     response = client.get(url)
#     assert response.status_code == 200

from django.urls import reverse
from django.utils import timezone
from orders.models import Discount
from project.constants import DECIMAL_PLACES, MAX_DIGITS
from project.model_choices import DiscountTypes


def test_cart(client, login_client, product_factory, faker):
    url = reverse('cart')
    response = client.get(url, follow=True)
    assert response.status_code == 200
    assert '/en' + response.redirect_chain[0][0] == reverse(
        'login') + f'?next={url}'
    assert response.redirect_chain[0][1] == 302

    client, user = login_client()
    response = client.get(url)
    assert response.status_code == 200
    assert not response.context['order_items']
    order = response.context['order']
    assert order
    assert not order.order_items.exists()

    product = product_factory()
    data = {
        'product_id': faker.uuid4()
    }
    response = client.post(reverse('cart_action', args=('add',)), data=data,
                           follow=True)
    assert response.status_code == 200
    assert not order.order_items.exists()
    data['product_id'] = str(product.id)
    response = client.post(reverse('cart_action', args=('add',)), data=data,
                           follow=True)
    assert response.status_code == 200
    order_item = order.order_items.first()
    assert order_item.product == product
    assert order_item.quantity == 1
    assert order_item.price == product.price

    data = {
        'item_1': str(order_item.id),
        'quantity_1': 5,
    }
    response = client.post(url, data=data, follow=True)
    assert response.status_code == 200
    order_item.refresh_from_db()
    assert order_item.quantity == data['quantity_1']

    # discounts
    assert not order.discount
    discount = Discount.objects.create(
        code=faker.word(),
        # valid_until=timezone.now(),
        amount=faker.pydecimal(
            min_value=0,
            left_digits=MAX_DIGITS - DECIMAL_PLACES,
            right_digits=DECIMAL_PLACES,
        )
    )
    data = {
        'discount': discount.code,
    }
    assert discount.is_valid
    response = client.post(url, data=data, follow=True)
    assert response.status_code == 200
    assert not order.discount
    order.refresh_from_db()
    assert order.discount

    discount.valid_until = timezone.now()
    assert not discount.is_valid

    # clear
    client.post(reverse('cart_action', args=('clear',)), data={}, follow=True)
    assert not order.order_items.exists()

    # remove
    quantity = 3
    products = []
    for _ in range(quantity):
        product = product_factory()
        data = {
            'product_id': str(product.id)
        }

        client.post(reverse('cart_action', args=('add',)), data=data,
                    follow=True)
        products.append(product)
    assert order.order_items.count() == len(products)

    data = {
        'order_item_id': order.order_items.values()[0]['id']
    }
    response = client.post(reverse('cart_action', args=('remove',)), data=data,
                           follow=True)
    assert response.status_code == 200
    assert order.order_items.count() == (len(products) - 1)

    # pay
    assert order.is_current_order
    response = client.post(reverse('cart_action', args=('pay',)), follow=True)
    assert response.status_code == 200
    order.refresh_from_db()
    assert not order.is_active
    assert order.is_paid

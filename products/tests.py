import os
import PyPDF2

from django.urls import reverse
from random import randint

from products.models import Product
from project.settings import BASE_DIR


def test_products_list(client, product_factory, faker):
    for _ in range((randint(3, 20))):
        product_factory()
    url = reverse('products')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.context['products']) == Product.objects.count()


def test_product_detail(client, product_factory, faker):
    product_ex = product_factory()
    url = reverse('products')
    response = client.get(url, follow=True)
    assert response.status_code == 200
    response = client.get(reverse('product', kwargs={'pk': faker.uuid4()}))
    assert response.status_code == 404
    assert response.context.get('exception') == \
           'No product found matching the query'
    response = client.get(
        reverse('product', kwargs={'pk': product_ex.id}))
    assert response.status_code == 200
    assert product_ex == response.context['products']


# def test_product_by_category(client, product_factory, category_factory, faker):
#     category = category_factory()
#     breakpoint()
#     for _ in range((randint(3, 20))):
#         product_factory(categories=category)


def test_export_csv(client, product_factory, faker):
    quantity = (randint(3, 20))
    file_path = os.path.join(BASE_DIR, 'test_products.csv')
    for _ in range(quantity):
        product_factory()
    url = reverse('products_to_csv')
    response = client.get(url)
    assert response.status_code == 200
    attachment_data = response.content
    with open(file_path, mode='wb') as f:
        f.write(attachment_data)
    f_content = []
    with open(file_path, mode='r') as f:
        for line in f:
            f_content.append(line.strip())
    assert f_content
    assert len(f_content) == (quantity + 1)
    os.remove(file_path)


def test_export_to_pdf(client, product_factory, faker):
    quantity = (randint(50, 100))
    file_path = os.path.join(BASE_DIR, 'test_products.pdf')
    for _ in range(quantity):
        product_factory()
    url = reverse('products_to_pdf')
    response = client.get(url)
    assert response.status_code == 200
    attachment_data = response.content
    with open(file_path, mode='wb') as f:
        f.write(attachment_data)
    pdf_file = open(file_path, 'rb')
    # creating a pdf reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    # printing number of pages in pdf file
    pdf_content = []
    rows = 0
    for page in range(len(pdf_reader.pages)):
        # creating a page object
        page_obj = pdf_reader.pages[page]
        pdf_content.append(page_obj.extract_text())
        rows += len(pdf_content[page].split('\n'))
    # closing the pdf file object
    pdf_file.close()
    assert rows == (quantity + 2)
    os.remove(file_path)


def test_import_csv(client, login_staff, product_factory, faker):
    # creating products
    quantity = (randint(3, 20))
    file_path = os.path.join(BASE_DIR, 'test_products.csv')
    for _ in range(quantity):
        product_factory()
    url = reverse('products_to_csv')
    response = client.get(url)
    assert response.status_code == 200
    # creating csv file
    attachment_data = response.content
    with open(file_path, mode='wb') as f:
        f.write(attachment_data)
    url = reverse('products')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.context['products']) == Product.objects.count()
    assert quantity == Product.objects.count()
    Product.objects.all().delete()
    url = reverse('products')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.context['products']) == Product.objects.count() == 0
    # testing import csv
    url = reverse('products_from_csv')
    client, user = login_staff()
    data = {
        'file': file_path
    }
    response = client.post(url, data=data, follow=True)
    assert response.status_code == 200
    url = reverse('products')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.context['products']) == Product.objects.count()
    os.remove(file_path)

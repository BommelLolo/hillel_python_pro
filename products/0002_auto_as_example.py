# Generated by Django 4.1.7 on 2023-03-29 18:46

from django.db import migrations
from faker import Faker

fake = Faker()


def start(apps, schema_editor):
    Product = apps.get_model('products', 'Product')
    Category = apps.get_model('products', 'Category')

    for _ in range(100):
        product = Product.objects.create(
            name=fake.word(),
            description=fake.sentence(),
            sku=fake.random_number(),
            price=fake.pydecimal(left_digits=4, right_digits=2, positive=True)
        )
        product.categories.add(
            Category.objects.create(
                name=fake.word(),
                description=fake.sentence(),
            )
        )

    # for better efficiency will be better to use 1 query to DB like next:
    # products = []
    # for _ in range(1000):
    #     products.append(
    #         Product(
    #             name=fake.word(),
    #             description=fake.sentence(),
    #             sku=fake.random_number(),
    #             price=fake.pydecimal(left_digits=4, right_digits=2, positive=True)
    #         )
    #     )
    # Product.objects.bulk_create(products)


def end(apps, schema_editor):
    Product = apps.get_model('products', 'Product')
    Product.objects.all().delete()
    Category = apps.get_model('products', 'Category')
    Category.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            start,
            end
        )
    ]

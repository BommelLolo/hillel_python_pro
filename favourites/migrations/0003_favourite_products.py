# Generated by Django 4.2 on 2023-05-25 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20230521_1845'),
        ('favourites', '0002_remove_favourite_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='favourite',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='favourites', to='products.product'),
        ),
    ]

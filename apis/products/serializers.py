from rest_framework import serializers

from products.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'image', 'sku',
                  'created_at', 'updated_at', 'categories', 'category_name')

    def get_category_name(self, obj):
        return obj.categories.values_list('name', flat=True)


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'image', 'sku',
                  'created_at', 'updated_at', 'categories', 'category_name')

    def get_category_name(self, obj):
        return obj.categories.values_list('name', flat=True)
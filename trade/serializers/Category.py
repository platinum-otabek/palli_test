from rest_framework import serializers

from trade.models.Category import CategoryModel
from trade.models.Product import ProductModel
from trade.serializers.Product import ProductSerializer


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ('name',)


class CategoryListSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = CategoryModel
        fields = ('name', 'products')

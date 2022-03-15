from rest_framework import serializers

from trade.models.Product import ProductModel


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'


class ProductHighDemandSerializer(serializers.Serializer):
    product_name = serializers.CharField(source='product__name')
    quantity_sum = serializers.IntegerField(source='quantity__sum')


class BulkProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ('id', 'price', 'name', 'bulk_products')


class NumberOfProductsInYearSerializer(serializers.Serializer):
    country = serializers.CharField(source='order__customer__country')
    quantity_sum = serializers.IntegerField(source='quantity__sum')

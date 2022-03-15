from rest_framework import serializers

from trade.models.Order import OrderModel


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'


class OrderSerializerWithCustomerName(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer', read_only=True)

    class Meta:
        model = OrderModel
        fields = ('id', 'date', 'customer_name')

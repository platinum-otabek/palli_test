from rest_framework import serializers

from trade.models.Invoice import InvoiceModel


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceModel
        fields = '__all__'

from rest_framework import serializers

from trade.models.Invoice import InvoiceModel
from trade.models.Payment import PaymentModel


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentModel
        fields = '__all__'


class PaymentReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceModel
        fields = ('payment_reminder', 'id')

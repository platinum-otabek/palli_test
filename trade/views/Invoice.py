import datetime

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from trade.models.Invoice import InvoiceModel
from trade.models.Payment import PaymentModel
from trade.serializers.Invoice import InvoiceSerializer
from trade.serializers.Payment import PaymentReminderSerializer


class InvoiceExpiredViews(APIView):
    def get(self, request):
        invoices = InvoiceModel.objects.filter(due__lt=datetime.datetime.now())
        invoice_serializer = InvoiceSerializer(invoices, many=True)
        return Response(data=invoice_serializer.data)


class OverpaidInvoicesView(generics.ListAPIView):
    queryset = PaymentModel.objects.all()
    serializer_class = PaymentReminderSerializer

from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from trade.models.Invoice import InvoiceModel
from trade.models.Payment import PaymentModel
from trade.serializers.Payment import PaymentSerializer, PaymentReminderSerializer


class PaymentWithInvoiceApiView(APIView):

    def post(self, request, *args, **kwargs):
        payment_serializer = PaymentSerializer(data=request.data)
        if payment_serializer.is_valid():
            payment_serializer.save()
            return Response(payment_serializer.data, status=status.HTTP_201_CREATED)
        return Response(payment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentDetailView(generics.ListAPIView):
    queryset = InvoiceModel.objects.all()
    serializer_class = PaymentReminderSerializer

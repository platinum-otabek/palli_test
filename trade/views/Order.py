import datetime

from django.db.models import Exists, OuterRef
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from trade.models.Detail import DetailModel
from trade.models.Invoice import InvoiceModel
from trade.models.Order import OrderModel
from trade.models.Product import ProductModel
from trade.serializers.Detail import DetailSerializer
from trade.serializers.Invoice import InvoiceSerializer
from trade.serializers.Order import OrderSerializer


class OrderCreateApiView(APIView):
    def post(self, request):
        serializer_order = OrderSerializer(data=request.data)

        if serializer_order.is_valid():
            serializer_order.save()
            request.data['order'] = serializer_order.data['id']
            product = get_object_or_404(ProductModel, pk=request.data['product'])
            request.data['amount'] = float(request.data['quantity']) * float(product.price)
            serializer_detail = DetailSerializer(data=request.data)
            serializer_invoice = InvoiceSerializer(data=request.data)
            if serializer_detail.is_valid():
                serializer_detail.save()
            else:
                return Response(serializer_detail.errors, status=status.HTTP_400_BAD_REQUEST)

            if serializer_invoice.is_valid():
                serializer_invoice.save()
            else:
                return Response(serializer_invoice.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(data={'status': "SUCCESS", "invoice_number": serializer_invoice.data['id']},
                            status=status.HTTP_201_CREATED)
        return Response(serializer_order.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(APIView):
    def get(self, request, *args, **kwargs):
        order_detail = DetailModel.objects.filter(order_id=kwargs['order_id']) \
            .select_related("product")
        serializer = DetailSerializer(order_detail, many=True)
        return Response(data={'order': serializer.data[0], 'product': str(order_detail[0].product)})


class OrderWithoutDetailView(APIView):
    def get(self, request, *args, **kwargs):
        orders = OrderModel.objects.filter(
            ~Exists(DetailModel.objects.filter(order__id=OuterRef('pk'))),
            date__lt=datetime.date(2016, 9, 6)
        )
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class OrderWithOutInvoiceView(APIView):
    def get(self, request):
        orders = OrderModel.objects.filter(
            ~Exists(InvoiceModel.objects.filter(order__id=OuterRef('pk')))
        )
        details = DetailModel.objects.filter(order__in=orders).select_related('product')
        data = []
        for i in range(len(details)):
            data.append({
                'order_id': str(orders[i]),
                'product_name': details[i].product.name,
                'product_price': details[i].product.price,
                'quantity': details[i].quantity
            })
        return Response(data)

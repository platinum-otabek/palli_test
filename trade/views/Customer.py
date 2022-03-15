from django.db.models import Exists, OuterRef
from rest_framework.response import Response
from rest_framework.views import APIView

from trade.models.Customer import CustomerModel
from trade.models.Order import OrderModel
from trade.serializers.Customer import CustomerSerializer
from trade.serializers.Order import OrderSerializerWithCustomerName


class CustomerWithoutOrdersView(APIView):
    def get(self, request):
        customers = CustomerModel.objects.filter(
            ~Exists(OrderModel.objects.filter(customer__id=OuterRef('pk'),
                                              date__range=["2016-1-1", "2017-1-1"])),

        )
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)


class CustomerLastOrdersView(APIView):
    def get(self, request):
        customers = OrderModel.objects.order_by('customer__name', '-date') \
            .distinct('customer__name')
        serializer = OrderSerializerWithCustomerName(customers, many=True)
        return Response(serializer.data)

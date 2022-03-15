from django.db.models import Sum
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from trade.models.Detail import DetailModel
from trade.models.Product import ProductModel
from trade.serializers.Product import ProductSerializer, ProductHighDemandSerializer, NumberOfProductsInYearSerializer


class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer


class ProductDetailApiView(APIView):
    def get(self, request, *args, **kwargs):
        product = get_object_or_404(ProductModel, pk=kwargs['product_id'])
        product_serializer = ProductSerializer(product)
        return Response(data=product_serializer.data)


class HighDemandProducts(APIView):
    def get(self, request):
        high_demand_products = DetailModel.objects.values('product__name').annotate(Sum('quantity')) \
            .filter(quantity__sum__gt=10)
        serializer = ProductHighDemandSerializer(high_demand_products, many=True)
        return Response(serializer.data)


class BulkProductsView(APIView):
    def get(self, request):
        bulk_products = DetailModel.objects.filter(quantity__gt=6) \
            .select_related('product')
        data = []
        for product in bulk_products:
            data.append({
                'id': product.product.id,
                'price': product.product.price,
                'name': str(product.product),
            })

        return Response(data=data)


class NumberOfProductsInYearView(APIView):
    def get(self, request):
        products = DetailModel.objects.values('order__customer__country') \
            .annotate(Sum('quantity'))
        orders = OrderModel.objects.filter(id__in=products, date__range=["2022-01-01", "2022-12-31"])
        serializer = NumberOfProductsInYearSerializer(products, many=True)
        return Response(serializer.data)

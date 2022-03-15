from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from trade.models.Category import CategoryModel
from trade.models.Product import ProductModel
from trade.serializers.Category import CategoryListSerializer, CategoryCreateSerializer


class CategoryListCreateApiView(generics.ListCreateAPIView, viewsets.GenericViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            self.serializer_class = CategoryListSerializer
        elif self.action == 'create':
            self.serializer_class = CategoryCreateSerializer
        return self.serializer_class


class CategoryProductDetail(APIView):
    def get(self, request, *args, **kwargs):
        product = get_object_or_404(ProductModel, pk=kwargs['product_id'])
        category = CategoryModel.objects.filter(pk=product.category.pk)
        category_serializer = CategoryListSerializer(category, many=True)
        return Response(data=category_serializer.data)

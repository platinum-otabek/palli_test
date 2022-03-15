from django.db import models
from django.db.models import Sum


class ProductModel(models.Model):
    name = models.CharField(max_length=14, default='no name')
    category = models.ForeignKey('CategoryModel', on_delete=models.CASCADE, related_name='products')
    description = models.CharField(max_length=20, default='')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.CharField(max_length=1024)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


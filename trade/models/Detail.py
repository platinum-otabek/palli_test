from django.db import models
from django.db.models import Sum

from trade.models.Order import OrderModel
from trade.models.Product import ProductModel


class DetailModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.DO_NOTHING, related_name='detail')
    quantity = models.SmallIntegerField()

    class Meta:
        verbose_name = 'Order detail'
        verbose_name_plural = 'Order details'


from django.db import models


class OrderModel(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey('CustomerModel', on_delete=models.PROTECT, related_name='customer')

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return str(self.pk)

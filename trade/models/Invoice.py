import datetime

from django.db import models
from django.db.models import Sum

from trade.models.Order import OrderModel


class InvoiceModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    issued = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField(blank=True)

    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'

    def __str__(self):
        return str(self.order)

    def save(self, *args, **kwargs):
        self.due = datetime.datetime.now() + datetime.timedelta(days=7)
        super().save(*args, **kwargs)

    def payment_reminder(self):
        total = self.paymentmodel_set.aggregate(total_income=Sum('amount'))['total_income']
        if total and total > self.amount:
            return total - self.amount
        else:
            return "No payment"

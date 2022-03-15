from django.db import models

from trade.models.Invoice import InvoiceModel


class PaymentModel(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    invoice = models.ForeignKey(InvoiceModel, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        return str(self.invoice)

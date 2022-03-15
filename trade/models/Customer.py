from django.db import models


class CustomerModel(models.Model):
    name = models.CharField(max_length=14, default='no name')
    country = models.CharField(max_length=3, default='UZ')
    address = models.TextField()
    phone = models.CharField(max_length=50, default='')

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.name

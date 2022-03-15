from django.db import models


class CategoryModel(models.Model):
    name = models.CharField(max_length=50, default='')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

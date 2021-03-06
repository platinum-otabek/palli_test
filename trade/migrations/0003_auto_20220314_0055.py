# Generated by Django 3.1.6 on 2022-03-14 00:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_auto_20220313_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicemodel',
            name='due',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 14, 0, 55, 14, 326942)),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='trade.categorymodel'),
        ),
    ]

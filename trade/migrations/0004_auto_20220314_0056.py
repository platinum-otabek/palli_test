# Generated by Django 3.1.6 on 2022-03-14 00:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_auto_20220314_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicemodel',
            name='due',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

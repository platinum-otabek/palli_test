# Generated by Django 3.1.6 on 2022-03-14 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0006_auto_20220314_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicemodel',
            name='due',
            field=models.DateTimeField(blank=True),
        ),
    ]

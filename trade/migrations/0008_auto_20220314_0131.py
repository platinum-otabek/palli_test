# Generated by Django 3.1.6 on 2022-03-14 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0007_auto_20220314_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailmodel',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='detail', to='trade.productmodel'),
        ),
    ]

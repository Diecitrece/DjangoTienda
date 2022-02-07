# Generated by Django 3.2.3 on 2021-05-25 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormsApp', '0006_auto_20210525_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineasventa',
            name='Cantidad',
            field=models.IntegerField(default=1, max_length=5),
        ),
        migrations.AlterField(
            model_name='venta',
            name='TotalVenta',
            field=models.FloatField(default=0, max_length=9),
        ),
    ]

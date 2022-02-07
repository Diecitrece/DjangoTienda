# Generated by Django 3.2.3 on 2021-05-25 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormsApp', '0005_lineasventa_precioporlinea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineasventa',
            name='PrecioPorLinea',
            field=models.FloatField(default=0, max_length=9),
        ),
        migrations.AlterField(
            model_name='venta',
            name='TotalVenta',
            field=models.FloatField(blank=True, default=0, max_length=9, null=True),
        ),
    ]

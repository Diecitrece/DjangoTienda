# Generated by Django 3.2.3 on 2021-05-24 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FormsApp', '0002_alter_venta_totalventa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineasventa',
            name='idVenta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FormsApp.venta'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-03 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0002_alter_shop_city_alter_shop_street_alter_street_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='street',
            name='city',
            field=models.CharField(max_length=50),
        ),
    ]

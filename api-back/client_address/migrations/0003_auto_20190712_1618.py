# Generated by Django 2.2.3 on 2019-07-12 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_address', '0002_clientaddress_zip_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientaddress',
            name='zip_address',
            field=models.CharField(max_length=15),
        ),
    ]

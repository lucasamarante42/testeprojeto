# Generated by Django 2.2.3 on 2019-07-11 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20190711_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='cpf',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]

# Generated by Django 2.2.3 on 2019-07-11 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20190711_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]

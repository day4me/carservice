# Generated by Django 2.2.1 on 2019-06-05 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_request_date_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='car',
            field=models.CharField(default='Автомобіль', max_length=100, verbose_name='Автомобіль'),
        ),
    ]

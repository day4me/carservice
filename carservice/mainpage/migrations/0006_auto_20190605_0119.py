# Generated by Django 2.2.1 on 2019-06-05 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_services'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='problem',
        ),
        migrations.AddField(
            model_name='request',
            name='add_info',
            field=models.TextField(default='', verbose_name='Додаткова інформація'),
        ),
        migrations.AddField(
            model_name='request',
            name='service',
            field=models.CharField(default='Name', max_length=50, verbose_name='Послуга'),
        ),
    ]

# Generated by Django 2.2.1 on 2019-06-05 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0008_auto_20190605_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.Services', verbose_name='Produktart'),
        ),
    ]

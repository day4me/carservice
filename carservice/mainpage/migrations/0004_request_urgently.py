# Generated by Django 2.2.1 on 2019-06-05 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_auto_20190605_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='urgently',
            field=models.BooleanField(default=False, verbose_name='Терміново'),
        ),
    ]
# Generated by Django 2.2.1 on 2019-06-07 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0016_auto_20190607_1814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='state',
            new_name='status',
        ),
    ]

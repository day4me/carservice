# Generated by Django 2.2.1 on 2019-06-08 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0017_auto_20190607_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('Не підтверджено', 'Не підтверджено'), ('Підтверджено', 'Підтверджено'), ('Виконується', 'Виконується'), ('Виконано', 'Виконано'), ('Оплачено', 'Оплачено')], default='Не підтверджено', max_length=20, verbose_name='Статус'),
        ),
    ]
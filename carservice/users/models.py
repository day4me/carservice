from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(verbose_name=('Номер телефону'))
    vip_user = models.BooleanField(default=False, verbose_name=('Постійний клієнт'))

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Додаткова інформація'
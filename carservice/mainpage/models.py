from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date

## Таблиця послуг
class Services(models.Model):
    
    name = models.CharField(max_length=50, default='Name', verbose_name=('Назва послуги'))
    price = models.IntegerField(default=0, verbose_name=('Ціна послуги(грн)'))

    def __str__(self):
        return '%s (%s грн.)' % (self.name, self.price)

    class Meta:
        verbose_name_plural = "Послуги"


## Таблиця замовлень
class Request(models.Model):

    not_accepted = "Не підтверджено"
    accepted = "Підтверджено"
    is_executed = "Виконується"
    done = "Виконано"
    paid = "Оплачено"

    alfa = "Alfa Romeo"
    Aston = "Aston Martin"
    audi = "Audi"
    bmw = "BMW"
    chery = "Chery"
    chevrolet = "Chevrolet"
    chrysler = "Chrysler"
    citro = "Citroen"
    dacia = "Dacia"
    daweoo = "Daweoo"
    dodge = "Dodge"
    fiat = "Fiat"
    ford = "Ford"
    geely ="Geely"
    honda = "Honda"
    hyundai = "Hyundai"
    infiniti = "Infiniti"
    jaguar = "Jaguar"
    jeep = "Jeep"
    kia = "Kia"
    lexus = "Lexus"
    mazda = "Mazda"
    mers = "Mercedes-Benz"
    mitsu = "Mitsubishi"
    nissan = "Nissan"
    opel = "Opel"
    pego = "Peugeot"
    reno = "Renault"
    seat = "Seat"
    skoda = "Skoda"
    subaru = "Subaru"
    toyota = "Toyota"
    vw = "Volkswagen"
    volvo = "Volvo"

    BRAND_CHOICES = [
        (alfa, "Alfa Romeo"),
        (Aston, "Aston Martin"),
        (audi, "Audi"),
        (bmw, "BMW"),
        (chery, "Chery"),
        (chevrolet, "Chevrolet"),
        (chrysler, "Chrysler"),
        (citro, "Citroen"),
        (dacia, "Dacia"),
        (daweoo, "Daweoo"),
        (dodge, "Dodge"),
        (fiat, "Fiat"),
        (ford, "Ford"),
        (geely, "Geely"),
        (honda, "Honda"),
        (hyundai, "Hyundai"),
        (infiniti, "Infiniti"),
        (jaguar, "Jaguar"),
        (jeep, "Jeep"),
        (kia, "Kia"),
        (lexus, "Lexus"),
        (mazda, "Mazda"),
        (mers, "Mercedes-Benz"),
        (mitsu, "Mitsubishi"),
        (nissan, "Nissan"),
        (opel, "Opel"),
        (pego, "Peugeot"),
        (reno, "Renault"),
        (seat, "Seat"),
        (skoda, "Skoda"),
        (subaru, "Subaru"),
        (toyota, "Toyota"),
        (vw, "Volkswagen"),
        (volvo, "Volvo"),
    ]

    STATE_CHOICES = [
            (not_accepted, "Не підтверджено"),
            (accepted, "Підтверджено"),
            (is_executed, "Виконується"),
            (done, "Виконано"),
            (paid, "Оплачено")
        ]

    car = models.CharField(max_length=30, choices=BRAND_CHOICES, default=alfa, verbose_name=('Автомобіль'))
    service = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name=('Послуги'))
    add_info = models.TextField(blank=True, default='', verbose_name=('Додаткова інформація'))
    date_begin = models.DateField(default=date.today, verbose_name=('Дата початку робити'))
    date_end = models.DateField(default=date.today, verbose_name=('Дата закінчення робити'))
    author = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name=('Користувач'))
    status = models.CharField(max_length=20, choices=STATE_CHOICES, default=not_accepted, verbose_name=('Статус'))
    urgently = models.BooleanField(default=False, verbose_name=('Терміново'))

    def __str__(self):
        return '%s - %s (%s): %s' % (self.author, self.car, self.date_begin, self.status)
    
    class Meta:
        verbose_name_plural = "Замовлення"

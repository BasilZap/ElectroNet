from django.utils import timezone

from django.db import models

from users.models import NULLABLE


def get_time():
    return timezone.datetime.now()


print(get_time())


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название продукта')
    model = models.CharField(max_length=100, verbose_name='Модель продукта')
    launch_date = models.DateTimeField(verbose_name='Дата выхода на рынок')

    def __str__(self):
        return f'Продукт - {self.name} {self.model} (дата выхода - {self.model}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name='Компания')
    email = models.EmailField(verbose_name='Электронная почта')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    building = models.IntegerField(verbose_name='Номер дома')
    product = models.ManyToManyField(Product, verbose_name='Продукт')
    distributor = models.ForeignKey('Company', default=None, on_delete=models.DO_NOTHING, verbose_name='Поставщик',
                                    **NULLABLE)
    debt = models.FloatField(default=0.0, verbose_name='Задолженность')
    creation_date = models.DateTimeField(default=get_time(), verbose_name='Дата создания', **NULLABLE)

    def __str__(self):
        return f'Компания - {self.name}, задолженность поставщику {self.distributor} - {self.debt}'

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

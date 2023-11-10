from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(verbose_name="ФИО", unique=True, max_length=100)
    contact = models.CharField(verbose_name="Контакт", blank=True, max_length=200)
    where_from = models.CharField(verbose_name="Источник заказа", blank=True, max_length=200)
    oder_details = models.CharField(verbose_name="Индивидуальные условия заказа", blank=True, max_length=200)
    address = models.CharField(verbose_name="Адрес доставки", blank=True, max_length=200)
    notes = models.CharField(verbose_name="Заметки", blank=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Order(models.Model):
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class OrderPosition(models.Model):
    class OrderStatus(models.IntegerChoices):
        ORDER_1 = 1, 'Поступил'
        ORDER_2 = 2, 'Собран'
        ORDER_3 = 3, 'Отправлен'
        ORDER_4 = 4, 'Срочно'

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, blank=True, null=True, on_delete=models.CASCADE)
    description = models.CharField(verbose_name="Примечание", blank=True, max_length=200)
    status = models.PositiveSmallIntegerField(choices=OrderStatus.choices, default=OrderStatus.ORDER_1)


    def __str__(self):
        return f'{self.status}'

    class Meta:
        verbose_name = "Позиция"
        verbose_name_plural = "Позиции"

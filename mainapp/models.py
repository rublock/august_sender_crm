from django.db import models


class Client(models.Model):
    name = models.CharField(verbose_name="ФИО", max_length=100)
    contact = models.CharField(verbose_name="Контакт", blank=True, max_length=200)
    where_from = models.CharField(verbose_name="Источник заказа", blank=True, max_length=200)
    oder_details = models.CharField(verbose_name="Индивидуальные условия заказа", blank=True, max_length=200)
    address = models.CharField(verbose_name="Адрес доставки", blank=True, max_length=200)
    notes = models.CharField(verbose_name="Заметки", blank=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Order(models.Model):

    description = models.CharField(verbose_name="Примечание", blank=True, max_length=100)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f'{self.description}'


class OrderPosition(models.Model):

    class OrderStatus(models.IntegerChoices):
        ORDER_1 = 1, 'Поступил'
        ORDER_2 = 2, 'Собран'
        ORDER_3 = 3, 'Отправлен'
        ORDER_4 = 4, 'Срочно'

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.CharField(verbose_name="Продукт", max_length=100)
    quantity = models.IntegerField(default=1)
    status = models.PositiveSmallIntegerField(choices=OrderStatus.choices, default=OrderStatus.ORDER_1)
    description = models.CharField(verbose_name="Примечание", blank=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.status}'

    class Meta:
        verbose_name = "Позиция"
        verbose_name_plural = "Позиции"

from django.db import models


class Client(models.Model):
    name = models.CharField(verbose_name="ФИО", max_length=100)
    contact = models.TextField(verbose_name="Контакт", blank=True, max_length=200)
    where_from = models.TextField(verbose_name="Источник заказа", blank=True, max_length=200)
    oder_details = models.TextField(verbose_name="Индивидуальные условия заказа", blank=True, max_length=200)
    address = models.TextField(verbose_name="Адрес доставки", blank=True, max_length=200)
    notes = models.TextField(verbose_name="Заметки", blank=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Product(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=100)
    material = models.CharField(verbose_name="Материал", blank=True, max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Изделие"
        verbose_name_plural = "Изделия"


class Order(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100)
    order_product = models.ManyToManyField(Product)
    ordr_client = models.ManyToManyField(Client)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

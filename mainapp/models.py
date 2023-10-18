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
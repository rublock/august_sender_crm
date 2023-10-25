from django import forms
from .models import Client, Order
 
class NewOrderForm(forms.Form):
    CHOICES = [
        (1, 'Поступил'),
        (2, 'Собран'),
        (3, 'Отправлен'),
        (4, 'Срочно')
    ]

    # order = forms.IntegerField(initial=Order.objects.all())
    client = forms.ModelChoiceField(queryset=Client.objects.all())
    product = forms.CharField(label="Продукт", max_length=100)
    quantity = forms.IntegerField(initial=1)
    description = forms.CharField(label="Примечание", max_length=200, widget=forms.Textarea(attrs={'rows':3}))
    status = forms.ChoiceField(choices=CHOICES, initial=1)

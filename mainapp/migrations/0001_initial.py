# Generated by Django 4.2.4 on 2023-10-26 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('contact', models.CharField(blank=True, max_length=200, verbose_name='Контакт')),
                ('where_from', models.CharField(blank=True, max_length=200, verbose_name='Источник заказа')),
                ('oder_details', models.CharField(blank=True, max_length=200, verbose_name='Индивидуальные условия заказа')),
                ('address', models.CharField(blank=True, max_length=200, verbose_name='Адрес доставки')),
                ('notes', models.CharField(blank=True, max_length=200, verbose_name='Заметки')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='Примечание')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='OrderPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100, verbose_name='Продукт')),
                ('quantity', models.IntegerField(default=1)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Поступил'), (2, 'Собран'), (3, 'Отправлен'), (4, 'Срочно')], default=1)),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Примечание')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.client')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.order')),
            ],
            options={
                'verbose_name': 'Позиция',
                'verbose_name_plural': 'Позиции',
            },
        ),
    ]

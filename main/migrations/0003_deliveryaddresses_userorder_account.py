# Generated by Django 4.1.7 on 2023-02-28 00:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_banners'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryAddresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300, verbose_name='Адрес')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Адрес доставки',
                'verbose_name_plural': 'Адреса доставки',
            },
        ),
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=300, verbose_name='Номер заказа')),
                ('items', models.JSONField(blank=True, null=True, verbose_name='Ордер лист')),
                ('payment_status', models.CharField(choices=[], max_length=100)),
                ('order_status', models.CharField(choices=[], max_length=100)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('total', models.IntegerField(blank=True, verbose_name='Цена')),
                ('payment_method', models.CharField(max_length=300, verbose_name='Способ оплаты')),
                ('way_get', models.CharField(max_length=300, verbose_name='Способ получения')),
                ('debt', models.IntegerField(blank=True, null=True, verbose_name='Задолжность (если есть)')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.deliveryaddresses')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Имя')),
                ('phone', models.CharField(max_length=300, verbose_name='Телефон')),
                ('email', models.CharField(max_length=300, verbose_name='Почта')),
                ('agents', models.CharField(max_length=300, verbose_name='Контрагенты')),
                ('address', models.CharField(max_length=300, verbose_name='Адреса')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-21 07:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dhm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('DeliveryId', models.AutoField(primary_key=True, serialize=False)),
                ('DeliveryOrderDateTime', models.DateTimeField()),
                ('DeliveryCompleteDateTime', models.DateTimeField()),
                ('ProductType', models.CharField(max_length=200)),
                ('Product', models.CharField(max_length=200)),
                ('Courier', models.CharField(max_length=200)),
                ('MarketingSource', models.CharField(max_length=200)),
                ('OrderTotalSum', models.PositiveIntegerField()),
                ('City', models.CharField(max_length=200)),
                ('Region', models.CharField(max_length=200)),
                ('Street', models.CharField(max_length=200)),
                ('Home', models.PositiveIntegerField()),
                ('Building', models.PositiveIntegerField()),
                ('Latitude', models.DecimalField(decimal_places=4, max_digits=5)),
                ('Longitude', models.DecimalField(decimal_places=4, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='DHMUser',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('ReportId', models.AutoField(primary_key=True, serialize=False)),
                ('TypeReport', models.CharField(max_length=200)),
                ('DateFrom', models.DateField()),
                ('DateTo', models.DateField()),
                ('DateTimeComposed', models.DateTimeField(auto_now=True)),
                ('PolygonSize', models.PositiveIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='delivery',
            name='UserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dhm.DHMUser'),
        ),
    ]
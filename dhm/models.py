# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class DHMUser(models.Model):

    """ Класс для табилцы в БД с пользователями. """

    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=200)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=200)


class DHMMarketingSource(models.Model):

    """ Класс для табилцы в БД с источниками рекламы. """

    MarketingSourceId = models.AutoField(primary_key=True)
    MarketingSourceName = models.CharField(max_length=200)
    UserId = models.ForeignKey(DHMUser, on_delete=models.CASCADE)


class DHMProductType(models.Model):

    """ Класс для табилцы в БД с типами товаров. """

    ProductTypeId = models.AutoField(primary_key=True)
    ProductTypeName = models.CharField(max_length=200)
    UserId = models.ForeignKey(DHMUser, on_delete=models.CASCADE)


class Report(models.Model):

    """ Класс для табилцы в БД с сохраненными ранее отчетами. """

    ReportId = models.AutoField(primary_key=True)
    TypeReport = models.CharField(max_length=200)
    DateFrom = models.DateField()
    DateTo = models.DateField()
    DateTimeComposed = models.DateTimeField(auto_now=True)
    PolygonSize = models.PositiveIntegerField()


class Delivery(models.Model):

    """ Класс для табилцы в БД с объектами доставки. """

    DeliveryId = models.AutoField(primary_key=True)
    UserId = models.ForeignKey(DHMUser, on_delete=models.CASCADE)
    DeliveryOrderDateTime = models.DateTimeField()
    DeliveryCompleteDateTime = models.DateTimeField()
    ProductType = models.CharField(max_length=200)
    Product = models.CharField(max_length=200)
    Courier = models.CharField(max_length=200)
    MarketingSource = models.CharField(max_length=200)
    OrderTotalSum = models.DecimalField(max_digits=10, decimal_places=4)
    City = models.CharField(max_length=200)
    Region = models.CharField(max_length=200)
    Street = models.CharField(max_length=200)
    Home = models.PositiveIntegerField()
    Building = models.PositiveIntegerField()
    Latitude = models.DecimalField(max_digits=5, decimal_places=4)
    Longitude = models.DecimalField(max_digits=5, decimal_places=4)

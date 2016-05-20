# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):

    """ Класс для табилцы в БД с пользователями. """

    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=200)
    Email = models.EmailField(unique=True)
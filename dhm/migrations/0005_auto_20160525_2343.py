# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-25 23:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dhm', '0004_dhmmarketingsource_dhmproducttype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dhmproducttype',
            old_name='ProductType',
            new_name='ProductTypeId',
        ),
    ]

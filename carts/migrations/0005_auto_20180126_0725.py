# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-26 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_auto_20180125_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]

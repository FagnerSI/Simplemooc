# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-31 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180731_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='é da equipe??'),
        ),
    ]

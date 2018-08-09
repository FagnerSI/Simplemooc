# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-02 14:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180801_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordreset',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resets', to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]
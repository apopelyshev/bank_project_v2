# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-11 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_delete_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_korp_kontrol',
            name='data_otveta_1_2',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data_korp_kontrol',
            name='data_otveta_1_3',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data_korp_kontrol',
            name='data_otveta_3_3',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]

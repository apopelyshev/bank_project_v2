# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-26 17:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20180224_2259'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.RemoveField(
            model_name='historicaldata111',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicaldocument',
            name='history_user',
        ),
        migrations.DeleteModel(
            name='HistoricalData111',
        ),
        migrations.DeleteModel(
            name='HistoricalDocument',
        ),
    ]

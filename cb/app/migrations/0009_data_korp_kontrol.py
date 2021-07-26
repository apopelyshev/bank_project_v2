# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-03 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data_korp_kontrol',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False, unique=True)),
                ('ogrn', models.IntegerField(unique=True)),
                ('data_proverki', models.CharField(blank=True, max_length=1000, null=True)),
                ('polucheno_2', models.CharField(blank=True, max_length=1000, null=True)),
                ('srok_dla_inspolnenia_2', models.CharField(blank=True, max_length=1000, null=True)),
                ('data_instechenia_sroka_inpolnenia_2', models.CharField(blank=True, max_length=1000, null=True)),
                ('dokumenti_predstavleni_2', models.CharField(blank=True, max_length=1000, null=True)),
                ('ispolneno_2', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]

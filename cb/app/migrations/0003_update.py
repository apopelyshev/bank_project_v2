# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-31 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aaa', models.IntegerField()),
                ('www', models.IntegerField()),
                ('qqq', models.IntegerField()),
                ('zzz', models.IntegerField()),
            ],
        ),
    ]

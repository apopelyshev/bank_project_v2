# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-10 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20180318_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_korp_kontrol',
            name='data_instechenia_sroka_inpolnenia_1',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='data_korp_kontrol',
            name='data_instechenia_sroka_inpolnenia_1_3',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='data_korp_kontrol',
            name='data_instechenia_sroka_inpolnenia_3_3',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='data_korp_kontrol',
            name='data_otveta_1_2',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='data_korp_kontrol',
            name='data_otveta_1_3',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='data_korp_kontrol',
            name='data_otveta_3_3',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='data_korp_kontrol',
            name='data_provedinia_3_1_1',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='data_korp_kontrol',
            name='data_sostavlenia_protokola_gosa',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='data_korp_kontrol',
            name='data_sostavlenia_spiska_lich_imeushih_pravo_na_uchastie_v_gosa',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='data_korp_kontrol',
            name='informaciaya_o_gosah_s_saitov_raskritiya_informacii',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='data_korp_kontrol',
            name='ispolneno_1',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='data_korp_kontrol',
            name='ispolneno_1_2',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='data_korp_kontrol',
            name='ispolneno_1_3',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='data_korp_kontrol',
            name='ispolneno_3_3',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='data_korp_kontrol',
            name='otvet_1_2',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='data_korp_kontrol',
            name='otvet_1_3',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='data_korp_kontrol',
            name='otvet_3_3',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='data_korp_kontrol',
            name='polucheno_3_3',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='data_korp_kontrol',
            name='povestka_dnia_gosa',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='data_korp_kontrol',
            name='predpisanie_ob_istrebovanii_documentov_3_3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='data_korp_kontrol',
            name='srok_dla_inspolnenia_1',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='data_korp_kontrol',
            name='srok_dla_inspolnenia_1_3',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='data_korp_kontrol',
            name='srok_dla_inspolnenia_3_3',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='data_korp_kontrol',
            name='sroki_provedenia_gosa_po_ustavu',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='data_korp_kontrol',
            name='zapros_o_predostavlenii_informacii_3_2',
            field=models.BooleanField(default=False),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-12 04:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('human_resources', '0002_auto_20170505_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoyaltyScheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LoyaltyTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loyalty_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('identification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='human_resources.Identification')),
            ],
        ),
    ]

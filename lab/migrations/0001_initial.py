# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-10 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='1', max_length=100)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-15 13:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sua', '0016_auto_20170715_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appeal',
            name='gsua',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sua.GSua'),
        ),
        migrations.AlterField(
            model_name='appeal',
            name='sua',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sua.Sua'),
        ),
    ]

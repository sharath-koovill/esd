# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-06-07 07:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20170605_0348'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='contacts',
            unique_together=set([]),
        ),
    ]

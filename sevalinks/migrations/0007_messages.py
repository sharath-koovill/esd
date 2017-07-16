# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-13 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sevalinks', '0006_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.IntegerField()),
                ('target_id', models.IntegerField()),
                ('send_date', models.DateTimeField(auto_now=True)),
                ('ack_date', models.DateTimeField(null=True)),
                ('message', models.TextField()),
            ],
        ),
    ]

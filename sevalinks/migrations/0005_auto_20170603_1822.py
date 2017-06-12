# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-06-03 18:22
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sevalinks', '0004_user_user_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_identifier',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
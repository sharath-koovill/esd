# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-04 20:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sevalinks', '0002_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('contact_status_created', models.DateTimeField(auto_now=True)),
                ('user_action_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='sevalinks.User')),
                ('user_one_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='sevalinks.User')),
                ('user_two_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='sevalinks.User')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='contacts',
            unique_together=set([('user_one_id', 'user_two_id')]),
        ),
    ]

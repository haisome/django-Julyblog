# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-20 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userprofile_midea_cardnum'),
    ]

    operations = [
        migrations.CreateModel(
            name='MideaUserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupid', models.CharField(default='default', max_length=100)),
                ('jid', models.CharField(default='default', max_length=100)),
                ('name', models.CharField(default='default', max_length=100)),
                ('sex', models.CharField(default='default', max_length=100)),
                ('email', models.CharField(default='default', max_length=100)),
                ('position', models.CharField(default='default', max_length=100)),
                ('number', models.CharField(default='default', max_length=100)),
                ('py', models.CharField(default='default', max_length=100)),
                ('pyinitials', models.CharField(default='default', max_length=100)),
            ],
        ),
    ]

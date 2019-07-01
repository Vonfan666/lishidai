#!/usr/bin/python3
# -*- coding:utf-8 -*-
#author=von-fan
# Generated by Django 2.2.2 on 2019-06-28 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('phone', models.CharField(max_length=11)),
                ('pwd', models.CharField(max_length=18)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'login',
            },
        ),
    ]
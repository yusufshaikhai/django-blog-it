# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-21 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_blog_it', '0018_auto_20190820_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='casestudies',
            name='meta_description',
            field=models.TextField(blank=True, max_length=160, null=True),
        ),
        migrations.AddField(
            model_name='casestudies',
            name='meta_keywords',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]

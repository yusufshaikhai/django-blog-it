# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-20 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_blog_it', '0017_auto_20190820_2217'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='casestudies',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='casestudies',
            name='slug',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]

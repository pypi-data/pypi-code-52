# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-12-05 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edxval', '0013_thirdpartytranscriptcredentialsstate_copy_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thirdpartytranscriptcredentialsstate',
            name='exists',
            field=models.NullBooleanField(default=False, help_text='Transcript credentials state'),
        ),
    ]

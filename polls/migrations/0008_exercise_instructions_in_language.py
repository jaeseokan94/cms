# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_languagesubtopic_subtopic_name_in_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='instructions_in_language',
            field=models.CharField(max_length=500, null=True),
        ),
    ]

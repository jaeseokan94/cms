# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 15:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20160223_1556'),
    ]

    operations = [
        migrations.RenameField(
            model_name='languagesubtopic',
            old_name='video_url',
            new_name='grammar_video_file',
        ),
    ]

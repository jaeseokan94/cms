# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20160216_1919'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('choice_answers', models.CharField(max_length=200)),
                ('correct_answer', models.CharField(max_length=200)),
            ],
        ),
    ]
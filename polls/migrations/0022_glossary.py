# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-20 12:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_exercise_question_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glossary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
                ('word_in_lang', models.CharField(max_length=50)),
                ('language_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Language')),
            ],
        ),
    ]
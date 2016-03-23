# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-23 03:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import polls.models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0026_auto_20160323_0157'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceDialectItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_url', models.FileField(blank=True, null=True, upload_to='', validators=[polls.models.validate_audio_extension])),
                ('resource_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.ResourceItem')),
            ],
        ),
    ]
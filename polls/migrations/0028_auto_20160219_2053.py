# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0027_auto_20160219_2045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='situationalvideo',
            options={'ordering': ('language_topic',)},
        ),
    ]

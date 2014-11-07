# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='created_at',
            field=models.DateTimeField(default=datetime.date(2014, 11, 5)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guest',
            name='start_time',
            field=models.DateTimeField(default=datetime.date(2014, 11, 5), blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guest',
            name='waiting_time',
            field=models.IntegerField(default=5, max_length=2, blank=True),
            preserve_default=False,
        ),
    ]

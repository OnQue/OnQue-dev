# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0003_auto_20141105_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='start_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='waiting_time',
            field=models.IntegerField(max_length=2, null=True, blank=True),
        ),
    ]

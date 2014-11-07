# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0002_auto_20141105_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='age',
            field=models.IntegerField(default=18, blank=True),
        ),
    ]

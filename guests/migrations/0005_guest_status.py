# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0004_auto_20141105_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='status',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]

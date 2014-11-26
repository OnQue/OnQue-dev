# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0008_auto_20141126_0549'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='no_show',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

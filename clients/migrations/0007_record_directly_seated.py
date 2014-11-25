# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_auto_20141125_0650'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='directly_seated',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0015_auto_20141126_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='feed_match',
            field=models.IntegerField(default=737, max_length=4, null=True, editable=False),
            preserve_default=True,
        ),
    ]

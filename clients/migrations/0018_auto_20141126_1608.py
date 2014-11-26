# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0017_auto_20141126_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='feed_match',
            field=models.IntegerField(default=676, max_length=4, null=True, editable=False),
        ),
    ]

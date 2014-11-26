# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0016_record_feed_match'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='Food',
            new_name='food',
        ),
        migrations.AlterField(
            model_name='record',
            name='feed_match',
            field=models.IntegerField(default=402, max_length=4, null=True, editable=False),
        ),
    ]

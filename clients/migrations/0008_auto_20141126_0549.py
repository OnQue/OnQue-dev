# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_record_directly_seated'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='record',
            field=models.ForeignKey(to='clients.Record', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='record',
            name='take_away',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

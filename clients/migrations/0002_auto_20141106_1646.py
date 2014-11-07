# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='seated',
            field=jsonfield.fields.JSONField(default={}, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='table',
            name='waiting_list',
            field=jsonfield.fields.JSONField(default={}, null=True),
            preserve_default=True,
        ),
    ]

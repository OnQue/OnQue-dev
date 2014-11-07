# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20141106_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='seated',
            field=jsonfield.fields.JSONField(default={b'seated': []}, null=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='waiting_list',
            field=jsonfield.fields.JSONField(default={b'waiting_list': []}, null=True),
        ),
    ]

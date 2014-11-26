# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0014_auto_20141126_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='visit_id',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='mobile',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='record',
            name='mobile',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='table',
            name='mobile',
            field=models.IntegerField(max_length=10, null=True, blank=True),
        ),
    ]

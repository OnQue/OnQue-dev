# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0013_record_visit_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='record',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='table',
            name='mobile',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]

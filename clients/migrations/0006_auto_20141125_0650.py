# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_record_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='table_num',
            field=models.CharField(default=b'0', max_length=32),
        ),
    ]

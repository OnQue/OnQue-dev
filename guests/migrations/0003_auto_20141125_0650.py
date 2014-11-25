# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0002_personalrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='table_no',
            field=models.CharField(default=b'0', max_length=32),
        ),
    ]

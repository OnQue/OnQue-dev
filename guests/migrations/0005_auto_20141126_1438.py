# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0004_auto_20141126_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='mobile',
            field=models.IntegerField(max_length=10, serialize=False, primary_key=True),
        ),
    ]

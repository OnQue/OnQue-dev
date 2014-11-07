# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0005_guest_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='current_rest',
            field=models.CharField(default=b'null', max_length=32),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='guest',
            name='table_no',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]

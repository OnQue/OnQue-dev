# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0009_record_no_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='first_login',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]

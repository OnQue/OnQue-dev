# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0006_auto_20141106_1659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='current_rest',
            new_name='current',
        ),
    ]

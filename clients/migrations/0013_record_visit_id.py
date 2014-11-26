# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0012_table_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='visit_id',
            field=models.IntegerField(default=uuid.uuid4, null=True, editable=False),
            preserve_default=True,
        ),
    ]

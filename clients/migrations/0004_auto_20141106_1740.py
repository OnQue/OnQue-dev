# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20141106_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='id',
        ),
        migrations.AlterField(
            model_name='table',
            name='user',
            field=models.ForeignKey(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]

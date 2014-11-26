# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0010_table_first_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='city',
            field=models.CharField(max_length=32, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='table',
            name='email',
            field=models.EmailField(max_length=60, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='table',
            name='first_name',
            field=models.CharField(max_length=32, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='table',
            name='last_name',
            field=models.CharField(max_length=32, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='table',
            name='mobile',
            field=models.IntegerField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
    ]

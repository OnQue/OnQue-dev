# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('mobile', models.IntegerField(max_length=10, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=32, blank=True)),
                ('age', models.IntegerField(blank=True)),
                ('restuarants', jsonfield.fields.JSONField(default={b'visited': []})),
                ('last_visited', jsonfield.fields.JSONField(default={b'date': b'', b'restuarant': b''})),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

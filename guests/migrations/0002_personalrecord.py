# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('restuarant', models.CharField(max_length=32, blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('guest', models.ForeignKey(to='guests.Guest')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

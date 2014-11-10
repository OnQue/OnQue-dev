# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('mobile', models.IntegerField(max_length=10)),
                ('age', models.IntegerField(max_length=2)),
                ('conversion', models.BooleanField(default=False)),
                ('bill', models.IntegerField(max_length=10, null=True, blank=True)),
                ('table_num', models.IntegerField(max_length=10, null=True, blank=True)),
                ('waiting', models.BooleanField(default=True)),
                ('seated', models.BooleanField(default=False)),
                ('no', models.IntegerField(default=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='table',
            fields=[
                ('user', models.ForeignKey(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('n_of_table', models.IntegerField(default=0)),
                ('status', jsonfield.fields.JSONField()),
                ('waiting_list', jsonfield.fields.JSONField(default={b'waiting_list': []}, null=True)),
                ('seated', jsonfield.fields.JSONField(default={b'seated': []}, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='record',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]

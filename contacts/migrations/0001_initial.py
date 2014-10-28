# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(default=None, max_length=255)),
                ('last_name', models.CharField(default=None, max_length=255)),
                ('email', models.EmailField(default=None, max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

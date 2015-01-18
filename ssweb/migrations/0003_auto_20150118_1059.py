# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ssweb', '0002_auto_20150118_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='ss_last_trans_time',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]

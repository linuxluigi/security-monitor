# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='w3af_server',
            name='Scan',
            field=models.ForeignKey(blank=True, to='monitoring.W3af_scan', null=True),
        ),
    ]

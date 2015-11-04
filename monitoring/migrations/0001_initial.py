# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='W3af_findings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('href', models.CharField(max_length=255, blank=True)),
                ('url', models.URLField(blank=True)),
                ('desc', models.TextField(null=True, blank=True)),
                ('long_description', models.TextField(null=True, blank=True)),
                ('plugin_name', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='W3af_scan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_scan', models.DateTimeField(default=django.utils.timezone.now)),
                ('stop_scan', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='W3af_server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server_name', models.CharField(default=b'localhost', max_length=50)),
                ('notice', models.CharField(max_length=255, blank=True)),
                ('host', models.URLField(default=b'http://127.0.0.1:5000/')),
                ('username', models.CharField(max_length=255, blank=True)),
                ('password', models.CharField(max_length=512, blank=True)),
                ('running', models.BooleanField(default=0)),
                ('last_scan', models.DateTimeField(null=True, blank=True)),
                ('registred', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('registred', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_scan', models.DateTimeField(null=True, blank=True)),
                ('cron', models.BooleanField(default=False)),
                ('User', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='w3af_scan',
            name='Website',
            field=models.ForeignKey(to='monitoring.Website'),
        ),
        migrations.AddField(
            model_name='w3af_findings',
            name='scan_object',
            field=models.ForeignKey(to='monitoring.W3af_scan'),
        ),
    ]

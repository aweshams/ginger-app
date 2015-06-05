# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=300, null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='vendors',
            name='start_time',
        ),
        migrations.AlterField(
            model_name='vendors',
            name='location',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='vendors',
            name='start_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]

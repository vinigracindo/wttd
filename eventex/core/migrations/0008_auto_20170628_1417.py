# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20170623_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='título')),
                ('start', models.TimeField(blank=True, null=True, verbose_name='início')),
                ('description', models.TextField(blank=True, verbose_name='descrição')),
                ('slots', models.IntegerField()),
                ('speakers', models.ManyToManyField(blank=True, to='core.Speaker', verbose_name='palestrantes')),
            ],
            options={
                'verbose_name': 'palestra',
                'verbose_name_plural': 'palestras',
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='talk',
            options={'verbose_name': 'palestra', 'verbose_name_plural': 'palestras'},
        ),
    ]

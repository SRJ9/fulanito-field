# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 13:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import swapfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('number', swapfield.fields.SwapIntegerField(unique_for_fields=[b'team'])),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Team'),
        ),
    ]
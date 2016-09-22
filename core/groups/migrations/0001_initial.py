# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 07:43
from __future__ import unicode_literals

import core.methods
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_usersandcourses_usersandunits'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to=core.methods.group_picture_upload_path_handler)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserAccount')),
            ],
        ),
    ]

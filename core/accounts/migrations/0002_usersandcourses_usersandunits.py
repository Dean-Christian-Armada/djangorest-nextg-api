# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 00:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20160921_0027'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersAndCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField(auto_now_add=True)),
                ('end', models.DateField(blank=True, null=True)),
                ('school_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.SchoolsAndCourses')),
                ('user_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserAccount')),
            ],
        ),
        migrations.CreateModel(
            name='UsersAndUnits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CoursesAndUnits')),
                ('user_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserAccount')),
            ],
        ),
    ]
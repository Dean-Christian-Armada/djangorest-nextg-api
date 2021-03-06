# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 00:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20160920_0737'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('code', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='CoursesAndUnits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolsAndCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Course')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.School')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('code', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='coursesandunits',
            name='school_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.SchoolsAndCourses'),
        ),
        migrations.AddField(
            model_name='coursesandunits',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Unit'),
        ),
    ]

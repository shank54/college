# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-21 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0002_auto_20180319_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sp2011',
            name='Catalog',
            field=models.CharField(max_length=550),
        ),
        migrations.AlterField(
            model_name='sp2011',
            name='Primary_Instructor',
            field=models.CharField(max_length=550),
        ),
        migrations.AlterField(
            model_name='sp2011',
            name='Section',
            field=models.CharField(max_length=550),
        ),
        migrations.AlterField(
            model_name='sp2011',
            name='Subject',
            field=models.CharField(max_length=550),
        ),
        migrations.AlterField(
            model_name='sp2011',
            name='Term',
            field=models.CharField(max_length=550),
        ),
        migrations.AlterField(
            model_name='sp2011',
            name='Title',
            field=models.CharField(max_length=550),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-16 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_username', models.CharField(max_length=150)),
                ('review_service', models.CharField(max_length=254)),
                ('rating', models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)], max_length=2)),
                ('review_title', models.CharField(max_length=100)),
                ('review_description', models.TextField()),
                ('review_image', models.ImageField(upload_to='images')),
                ('date_created', models.DateTimeField()),
                ('last_edited', models.DateTimeField()),
            ],
        ),
    ]

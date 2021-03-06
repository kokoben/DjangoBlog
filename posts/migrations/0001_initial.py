# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-22 10:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_posts', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('body', models.TextField()),
                ('archive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Archive')),
            ],
        ),
    ]

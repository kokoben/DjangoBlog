# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-23 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_num_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='num_likes',
            field=models.IntegerField(default=0, verbose_name='# of likes'),
        ),
    ]
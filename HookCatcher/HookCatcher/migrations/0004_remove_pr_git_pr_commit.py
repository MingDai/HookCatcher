# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-02 23:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HookCatcher', '0003_auto_20170728_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pr',
            name='git_pr_commit',
        ),
    ]

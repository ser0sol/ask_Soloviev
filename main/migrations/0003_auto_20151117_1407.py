# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20151110_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='tags',
        ),
        migrations.AddField(
            model_name='tag',
            name='question',
            field=models.ForeignKey(default=1, to='main.Question'),
            preserve_default=False,
        ),
    ]

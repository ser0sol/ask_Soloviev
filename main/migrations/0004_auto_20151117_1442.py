# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20151117_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='main.Tag'),
        ),
    ]

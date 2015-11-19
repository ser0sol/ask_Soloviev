# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20151117_1442'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='user',
            new_name='likes',
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=2),
        ),
    ]

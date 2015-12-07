# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watson', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchentry',
            name='title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='searchentry',
            name='url',
            field=models.TextField(blank=True),
        ),
    ]

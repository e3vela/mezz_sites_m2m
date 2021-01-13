# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('conf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='sites',
            field=models.ManyToManyField(to='sites.Site'),
        ),
    ]

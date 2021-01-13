# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('generic', '0003_auto_20170411_0504'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyword',
            name='sites',
            field=models.ManyToManyField(to='sites.Site'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('blog', '0003_auto_20170411_0504'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ('-publish_date',), 'verbose_name': 'Blog post', 'verbose_name_plural': 'Blog posts', 'permissions': (('can_modify_sites', 'Can modify sites'),)},
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='sites',
            field=models.ManyToManyField(to='sites.Site'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='sites',
            field=models.ManyToManyField(to='sites.Site'),
        ),
    ]

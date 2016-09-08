# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_tabs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tab',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='cmsplugin_tabs_tab', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='tabheader',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='cmsplugin_tabs_tabheader', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
    ]

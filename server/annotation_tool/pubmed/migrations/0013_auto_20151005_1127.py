# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0012_auto_20151005_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene',
            name='name',
            field=models.CharField(max_length=256),
        ),
    ]
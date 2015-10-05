# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed', '0011_auto_20151005_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene',
            name='alias_name',
            field=django.contrib.postgres.fields.ArrayField(null=True, base_field=models.CharField(max_length=128), size=None),
        ),
        migrations.AlterField(
            model_name='gene',
            name='alias_symbol',
            field=django.contrib.postgres.fields.ArrayField(null=True, base_field=models.CharField(max_length=128), size=None),
        ),
        migrations.AlterField(
            model_name='gene',
            name='bioparadigms_slc',
            field=models.CharField(null=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='gene',
            name='ccds_id',
            field=django.contrib.postgres.fields.ArrayField(null=True, base_field=models.CharField(max_length=128), size=None),
        ),
        migrations.AlterField(
            model_name='gene',
            name='cd',
            field=models.CharField(null=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='gene',
            name='cosmic',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='gene',
            name='ena',
            field=django.contrib.postgres.fields.ArrayField(null=True, base_field=models.CharField(max_length=128), size=None),
        ),
        migrations.AlterField(
            model_name='gene',
            name='ensembl_gene_id',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='gene',
            name='enzyme_id',
            field=django.contrib.postgres.fields.ArrayField(null=True, base_field=models.CharField(max_length=128), size=None),
        ),
        migrations.AlterField(
            model_name='gene',
            name='gene_family',
            field=django.contrib.postgres.fields.ArrayField(size=None, base_field=models.CharField(null=True, max_length=128), default=[]),
        ),
        migrations.AlterField(
            model_name='gene',
            name='hgnc_id',
            field=models.CharField(unique=True, db_index=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='gene',
            name='horde_id',
            field=models.CharField(null=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='gene',
            name='imgt',
            field=models.CharField(null=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='gene',
            name='intermediate_filament_db',
            field=models.CharField(null=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='gene',
            name='iuphar',
            field=models.CharField(null=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='gene',
            name='location',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='gene',
            name='location_sortable',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='gene',
            name='locus_group',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='gene',
            name='locus_type',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='gene',
            name='merops',
            field=models.CharField(null=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='gene',
            name='mgd_id',
            field=django.contrib.postgres.fields.ArrayField(null=True, base_field=models.CharField(max_length=128), size=None),
        ),
        migrations.AlterField(
            model_name='gene',
            name='mirbase',
            field=models.CharField(null=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='gene',
            name='orphanet',
            field=models.CharField(null=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='gene',
            name='prev_name',
            field=django.contrib.postgres.fields.ArrayField(null=True, base_field=models.CharField(max_length=128), size=None),
        ),
        migrations.AlterField(
            model_name='gene',
            name='prev_symbol',
            field=django.contrib.postgres.fields.ArrayField(null=True, base_field=models.CharField(max_length=128), size=None),
        ),
        migrations.AlterField(
            model_name='gene',
            name='refseq_accession',
            field=django.contrib.postgres.fields.ArrayField(null=True, base_field=models.CharField(max_length=128), size=None),
        ),
        migrations.AlterField(
            model_name='gene',
            name='rgd_id',
            field=django.contrib.postgres.fields.ArrayField(null=True, base_field=models.CharField(max_length=128), size=None),
        ),
        migrations.AlterField(
            model_name='gene',
            name='snornabase',
            field=models.CharField(null=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='gene',
            name='status',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='gene',
            name='symbol',
            field=models.CharField(db_index=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='gene',
            name='ucsc_id',
            field=models.CharField(null=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='gene',
            name='uniprot_ids',
            field=django.contrib.postgres.fields.ArrayField(null=True, base_field=models.CharField(max_length=128), size=None),
        ),
        migrations.AlterField(
            model_name='gene',
            name='vega_id',
            field=models.CharField(null=True, max_length=128),
        ),
    ]

# Generated by Django 3.1.7 on 2021-06-09 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myDatabase', '0009_auto_20210426_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='NwAttributes11Biorepository',
            fields=[
                ('product_code', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('long_description', models.TextField()),
                ('species', models.CharField(max_length=256)),
                ('tissue_type', models.CharField(max_length=256)),
                ('disease', models.CharField(max_length=256)),
                ('format', models.CharField(max_length=256)),
                ('cell_line', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'nw_attributes_11_biorepository',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NwAttributes12Molecularbiology',
            fields=[
                ('product_code', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('long_description', models.TextField()),
                ('accession_no', models.TextField()),
                ('gene_id', models.TextField()),
                ('gene_symbol', models.TextField()),
                ('gene_synonyms', models.TextField()),
                ('gene_description', models.TextField()),
                ('locus_id', models.TextField()),
                ('protein_families', models.TextField()),
                ('protein_pathways', models.TextField()),
                ('vector', models.TextField()),
                ('tag', models.TextField()),
                ('sequence_data', models.TextField()),
                ('aa_sequence', models.TextField()),
                ('application', models.TextField()),
                ('species', models.TextField()),
                ('cas_no', models.TextField()),
                ('selection_marker', models.TextField()),
                ('promoter', models.TextField()),
                ('tag_position', models.TextField()),
                ('purification', models.TextField()),
                ('vector_type', models.TextField()),
                ('sample_type', models.TextField()),
                ('concentration', models.TextField()),
                ('bead_size', models.TextField()),
                ('cell_type', models.TextField()),
            ],
            options={
                'db_table': 'nw_attributes_12_molecularbiology',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NwAttributes13Antibodies',
            fields=[
                ('product_code', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('long_description', models.TextField()),
                ('accession_no', models.TextField()),
                ('gene_id', models.TextField()),
                ('gene_symbol', models.TextField()),
                ('gene_synonyms', models.TextField()),
                ('gene_description', models.TextField()),
                ('locus_id', models.TextField()),
                ('protein_families', models.TextField()),
                ('protein_pathways', models.TextField()),
                ('host_species', models.TextField()),
                ('species_reactivity', models.TextField()),
                ('immunogen', models.TextField()),
                ('isotype', models.TextField()),
                ('clone_number', models.TextField()),
                ('formulation', models.TextField()),
                ('preservative', models.TextField()),
                ('concentration', models.TextField()),
                ('purification', models.TextField()),
                ('format', models.TextField()),
                ('application', models.TextField()),
                ('label_conjugate', models.TextField()),
                ('clonality', models.TextField()),
                ('type', models.TextField()),
                ('epitope', models.TextField()),
                ('target', models.TextField()),
                ('species', models.TextField()),
                ('tissue_type', models.TextField()),
                ('cell_line', models.TextField()),
            ],
            options={
                'db_table': 'nw_attributes_13_antibodies',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NwAttributes14Proteinspeptides',
            fields=[
                ('product_code', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('long_description', models.TextField()),
                ('accession_no', models.TextField()),
                ('gene_id', models.TextField()),
                ('gene_symbol', models.TextField()),
                ('gene_synonyms', models.TextField()),
                ('gene_description', models.TextField()),
                ('locus_id', models.TextField()),
                ('protein_families', models.TextField()),
                ('protein_pathways', models.TextField()),
                ('uniprot_id', models.TextField()),
                ('species', models.TextField()),
                ('expression_host', models.TextField()),
                ('predicted_mw', models.TextField()),
                ('determined_mw', models.TextField()),
                ('concentration', models.TextField()),
                ('aa_sequence', models.TextField()),
                ('activity', models.TextField()),
                ('format', models.TextField()),
                ('purity', models.TextField()),
                ('endotoxin', models.TextField()),
                ('tag', models.TextField()),
                ('formulation', models.TextField()),
                ('labeling_method', models.TextField()),
                ('target_specificity', models.TextField()),
                ('components', models.TextField()),
                ('preparation', models.TextField()),
                ('application', models.TextField()),
                ('tissue_type', models.TextField()),
                ('disease', models.TextField()),
                ('cell_line', models.TextField()),
                ('protocol_usage', models.TextField()),
                ('bead_size', models.TextField()),
                ('label_conjugate', models.TextField()),
                ('tag_position', models.TextField()),
            ],
            options={
                'db_table': 'nw_attributes_14_proteinspeptides',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NwAttributes15Cellscellculture',
            fields=[
                ('product_code', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('long_description', models.TextField()),
                ('accession_no', models.TextField()),
                ('gene_id', models.TextField()),
                ('gene_symbol', models.TextField()),
                ('gene_synonyms', models.TextField()),
                ('gene_description', models.TextField()),
                ('locus_id', models.TextField()),
                ('protein_families', models.TextField()),
                ('protein_pathways', models.TextField()),
                ('species', models.TextField()),
                ('tissue_type', models.TextField()),
                ('format', models.TextField()),
                ('application', models.TextField()),
                ('cell_line', models.TextField()),
                ('dimensions', models.TextField()),
                ('type', models.TextField()),
                ('cell_type', models.TextField()),
                ('vector', models.TextField()),
                ('tag', models.TextField()),
                ('sequence_data', models.TextField()),
                ('aa_sequence', models.TextField()),
                ('tag_position', models.TextField()),
                ('vector_type', models.TextField()),
                ('uniprot_id', models.TextField()),
                ('disease', models.TextField()),
                ('serotype', models.TextField()),
                ('formulation', models.TextField()),
                ('expression_host', models.TextField()),
                ('promoter', models.TextField()),
                ('protein_type', models.TextField()),
                ('protein', models.TextField()),
                ('mycoplasma_testing', models.TextField()),
                ('license_requirement', models.TextField()),
                ('expression', models.TextField()),
                ('tumorigenic', models.TextField()),
                ('components', models.TextField()),
                ('preparation', models.TextField()),
                ('selection_marker', models.TextField()),
            ],
            options={
                'db_table': 'nw_attributes_15_cellscellculture',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NwAttributes16Reagentslabware',
            fields=[
                ('product_code', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('long_description', models.TextField()),
                ('gene_id', models.TextField()),
                ('gene_symbol', models.TextField()),
                ('gene_synonyms', models.TextField()),
                ('gene_description', models.TextField()),
                ('protein_families', models.TextField()),
                ('protein_pathways', models.TextField()),
                ('cas_no', models.TextField()),
                ('purity', models.TextField()),
                ('mw', models.TextField()),
                ('alternative_names', models.TextField()),
                ('expression_host', models.TextField()),
                ('application', models.TextField()),
                ('concentration', models.TextField()),
                ('activity', models.TextField()),
                ('species', models.TextField()),
                ('activity_definition', models.TextField()),
                ('tissue_type', models.TextField()),
                ('carbohydrate_type', models.TextField()),
                ('oligosaccharide_length', models.TextField()),
                ('label_conjugate', models.TextField()),
            ],
            options={
                'db_table': 'nw_attributes_16_reagentslabware',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NwAttributes17Kitsassays',
            fields=[
                ('product_code', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('long_description', models.TextField()),
                ('accession_no', models.TextField()),
                ('gene_id', models.TextField()),
                ('gene_symbol', models.TextField()),
                ('gene_synonyms', models.TextField()),
                ('gene_description', models.TextField()),
                ('species_reactivity', models.TextField()),
                ('detection_range', models.TextField()),
                ('sensitivity', models.TextField()),
                ('application', models.TextField()),
                ('preservative', models.TextField()),
                ('components', models.TextField()),
                ('sample_type', models.TextField()),
                ('format', models.TextField()),
                ('elisa_format', models.TextField()),
                ('cross_reactivity', models.TextField()),
                ('specificity', models.TextField()),
                ('assay_time', models.TextField()),
                ('intra_assay_cv', models.TextField()),
                ('inter_assay_cv', models.TextField()),
            ],
            options={
                'db_table': 'nw_attributes_17_kitsassays',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NwAttributes18Bioseparationelectrophoresis',
            fields=[
                ('product_code', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('long_description', models.TextField()),
                ('application', models.TextField()),
                ('format', models.TextField()),
                ('bead_size', models.TextField()),
                ('type', models.TextField()),
            ],
            options={
                'db_table': 'nw_attributes_18_bioseparationelectrophoresis',
                'managed': False,
            },
        ),
    ]
# Generated by Django 3.1.7 on 2021-04-26 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myDatabase', '0005_auto_20210426_1233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currencies',
            options={'verbose_name_plural': 'Currencies'},
        ),
        migrations.AlterModelOptions(
            name='mastercurrencies',
            options={'verbose_name_plural': 'Master Currencies'},
        ),
        migrations.AlterModelOptions(
            name='nwcategoryids',
            options={},
        ),
        migrations.AlterModelOptions(
            name='nwcategorylowestnodes',
            options={},
        ),
        migrations.AlterModelOptions(
            name='nwresearchareaids',
            options={},
        ),
        migrations.AlterModelOptions(
            name='productrecords',
            options={},
        ),
        migrations.AlterModelOptions(
            name='productrecordstech',
            options={},
        ),
    ]
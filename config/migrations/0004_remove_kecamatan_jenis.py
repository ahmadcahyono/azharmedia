# Generated by Django 2.2.4 on 2019-12-03 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0003_auto_20191203_0946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kecamatan',
            name='jenis',
        ),
    ]

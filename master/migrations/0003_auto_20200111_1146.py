# Generated by Django 2.2.4 on 2020-01-11 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_auto_20200106_1448'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='karir',
            constraint=models.UniqueConstraint(fields=('karir',), name='karir'),
        ),
        migrations.AddConstraint(
            model_name='pekerjaan',
            constraint=models.UniqueConstraint(fields=('pekerjaan',), name='pekerjaan'),
        ),
    ]

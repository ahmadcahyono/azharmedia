# Generated by Django 2.2.4 on 2020-01-06 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jabatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jabatan', models.CharField(max_length=50)),
                ('tingkat', models.IntegerField()),
                ('upline', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Karir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('karir', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='brand',
            name='brand',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AddConstraint(
            model_name='brand',
            constraint=models.UniqueConstraint(fields=('brand',), name='brand'),
        ),
        migrations.AddConstraint(
            model_name='hubungankeluarga',
            constraint=models.UniqueConstraint(fields=('hubungan',), name='hubungan'),
        ),
        migrations.AddConstraint(
            model_name='jenjangpendidikan',
            constraint=models.UniqueConstraint(fields=('jenjang',), name='jenjang'),
        ),
        migrations.AddConstraint(
            model_name='kategori',
            constraint=models.UniqueConstraint(fields=('kategori',), name='kategori'),
        ),
        migrations.AddConstraint(
            model_name='nonformallist',
            constraint=models.UniqueConstraint(fields=('jenis',), name='jenis'),
        ),
    ]

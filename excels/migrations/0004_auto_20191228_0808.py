# Generated by Django 2.2.4 on 2019-12-28 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excels', '0003_auto_20191225_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='PemisahanKata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('kunciutama', models.CharField(max_length=15)),
                ('kunciawal', models.CharField(max_length=15)),
                ('kunciakhir', models.CharField(max_length=15)),
                ('deskripsi', models.TextField(blank=True)),
                ('jenis_data', models.CharField(blank=True, max_length=50)),
                ('tanggal_buat', models.DateTimeField(auto_now_add=True)),
                ('tanggal_edit', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.RenameField(
            model_name='jenjang',
            old_name='nama',
            new_name='pekerja',
        ),
        migrations.RenameField(
            model_name='jenjangkarir',
            old_name='nama',
            new_name='pekerja',
        ),
        migrations.RenameField(
            model_name='kemampuan',
            old_name='nama',
            new_name='pekerja',
        ),
        migrations.RenameField(
            model_name='kriteria',
            old_name='kunciakhir',
            new_name='kuncipencarian',
        ),
        migrations.RenameField(
            model_name='nonformalpendidikan',
            old_name='nama',
            new_name='pekerja',
        ),
        migrations.RenameField(
            model_name='pengalamankerja',
            old_name='nama',
            new_name='pekerja',
        ),
        migrations.RemoveField(
            model_name='kriteria',
            name='kunciawal',
        ),
        migrations.RemoveField(
            model_name='kriteria',
            name='kunciutama',
        ),
        migrations.AddField(
            model_name='keluarga',
            name='pekerja',
            field=models.IntegerField(default=0),
        ),
    ]

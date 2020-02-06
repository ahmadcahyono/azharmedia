# Generated by Django 2.2.4 on 2020-01-03 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('excels', '0011_auto_20200102_1132'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Jenjang',
        ),
        migrations.DeleteModel(
            name='JenjangKarir',
        ),
        migrations.RemoveField(
            model_name='karyawan',
            name='divisi',
        ),
        migrations.RemoveField(
            model_name='keluarga',
            name='hubungan',
        ),
        migrations.RemoveField(
            model_name='keluarga',
            name='pekerjaan',
        ),
        migrations.DeleteModel(
            name='Kemampuan',
        ),
        migrations.RemoveField(
            model_name='nonformalpendidikan',
            name='jenis',
        ),
        migrations.RemoveField(
            model_name='pelanggan',
            name='divisi_pelanggan',
        ),
        migrations.RemoveField(
            model_name='pendidikan',
            name='jenjang',
        ),
        migrations.DeleteModel(
            name='PengalamanKerja',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.RemoveField(
            model_name='produk',
            name='kategori',
        ),
        migrations.RemoveField(
            model_name='suplier',
            name='divisi_suplier',
        ),
        migrations.DeleteModel(
            name='Uploads',
        ),
        migrations.DeleteModel(
            name='Divisi',
        ),
        migrations.DeleteModel(
            name='HubunganKeluarga',
        ),
        migrations.DeleteModel(
            name='JenjangPendidikan',
        ),
        migrations.DeleteModel(
            name='Karyawan',
        ),
        migrations.DeleteModel(
            name='Kategori',
        ),
        migrations.DeleteModel(
            name='Keluarga',
        ),
        migrations.DeleteModel(
            name='NonFormalList',
        ),
        migrations.DeleteModel(
            name='NonFormalPendidikan',
        ),
        migrations.DeleteModel(
            name='Pekerjaan',
        ),
        migrations.DeleteModel(
            name='Pelanggan',
        ),
        migrations.DeleteModel(
            name='Pendidikan',
        ),
        migrations.DeleteModel(
            name='Produk',
        ),
        migrations.DeleteModel(
            name='Suplier',
        ),
    ]

# Generated by Django 2.2.4 on 2019-12-03 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_app_config_jenis_kabupaten_kecamatan_provinsi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kelurahan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_kel', models.CharField(max_length=10, unique=True)),
                ('id_kec', models.CharField(max_length=4)),
                ('nama', models.CharField(max_length=100)),
                ('jenis', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='kabupaten',
            name='id_kec',
        ),
        migrations.RemoveField(
            model_name='kabupaten',
            name='id_kel',
        ),
        migrations.AddField(
            model_name='kabupaten',
            name='id_kab',
            field=models.CharField(default='', max_length=4, unique=True),
        ),
        migrations.AddField(
            model_name='kabupaten',
            name='id_prop',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='kabupaten',
            name='jenis',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='kabupaten',
            name='nama',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

# Generated by Django 2.2.4 on 2019-12-03 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='App_Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Jenis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Kabupaten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_kel', models.CharField(max_length=10, unique=True)),
                ('id_kec', models.CharField(max_length=4)),
                ('nama', models.CharField(max_length=100)),
                ('jenis', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Kecamatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_kec', models.CharField(max_length=6, unique=True)),
                ('id_kab', models.CharField(max_length=4)),
                ('nama', models.CharField(max_length=100)),
                ('jenis', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Provinsi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_prov', models.CharField(max_length=2, unique=True)),
                ('nama', models.CharField(max_length=100)),
            ],
        ),
    ]

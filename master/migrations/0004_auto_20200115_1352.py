# Generated by Django 2.2.4 on 2020-01-15 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_auto_20200111_1146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jabatan',
            old_name='jabatan',
            new_name='namajabatan',
        ),
        migrations.AlterField(
            model_name='jabatan',
            name='tingkat',
            field=models.IntegerField(null='True'),
        ),
        migrations.AlterField(
            model_name='jabatan',
            name='upline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.Jabatan'),
        ),
    ]
# Generated by Django 4.2.5 on 2023-09-28 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=45)),
                ('ktp', models.CharField(max_length=16)),
                ('alamat', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'db_table': 'person',
            },
        ),
        migrations.CreateModel(
            name='PengalamanKerja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perusahaan', models.CharField(max_length=45)),
                ('jabatan', models.CharField(max_length=45)),
                ('tahun', models.CharField(max_length=4)),
                ('keterangan', models.TextField(blank=True, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.person')),
            ],
            options={
                'db_table': 'pengalaman_kerja',
            },
        ),
        migrations.CreateModel(
            name='Pendidikan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=45)),
                ('jurusan', models.CharField(max_length=45)),
                ('tahun_masuk', models.CharField(max_length=4)),
                ('tahun_lulus', models.CharField(max_length=4)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.person')),
            ],
            options={
                'db_table': 'pendidikan',
            },
        ),
    ]

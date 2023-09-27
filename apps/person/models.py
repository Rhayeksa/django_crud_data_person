from django.db import models

# Create your models here.


class Person(models.Model):
    nama = models.CharField(max_length=45)
    ktp = models.CharField(max_length=16)
    alamat = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "person"


class Pendidikan(models.Model):
    nama = models.CharField(max_length=45)
    jurusan = models.CharField(max_length=45)
    tahun_masuk = models.CharField(max_length=4)
    tahun_lulus = models.CharField(max_length=4)
    person = models.ForeignKey(to=Person, on_delete=models.CASCADE)

    class Meta:
        db_table = "pendidikan"


class PengalamanKerja(models.Model):
    perusahaan = models.CharField(max_length=45)
    jabatan = models.CharField(max_length=45)
    tahun = models.CharField(max_length=4)
    keterangan = models.TextField(null=True, blank=True)
    person = models.ForeignKey(to=Person, on_delete=models.CASCADE)

    class Meta:
        db_table = "pengalaman_kerja"

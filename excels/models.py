from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError
import os


class KategoriData(models.Model):
	nama_kategori_data = models.CharField(max_length = 50)
	keterangan_kategori_data = models.CharField(max_length = 100)
	def __str__(self):
		return self.nama_kategori_data


class JenisData(models.Model):
    nama_jd = models.CharField(max_length=50, unique=True)
    tabel_jd = models.CharField(max_length=50)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nama_jd'], name='nama_jd')
        ]

    def __str__(self):
        return self.nama_jd



class Kriteria(models.Model):
    nama = models.CharField(max_length=50)
    kuncipencarian = models.CharField(max_length=15)
    deskripsi = models.TextField(blank=True,)
    jenis_data = models.CharField(max_length=50, blank=True)
    tanggal_buat = models.DateTimeField(auto_now_add=True)
    tanggal_edit = models.DateTimeField(blank=True)
	
    def __str__(self):
	    return "%s %s" % (self.nama, self.kunciutama)

class KriteriaData(models.Model):
	id_kriteria = models.IntegerField()
	nama_tabel  = models.IntegerField()
	id_data = models.IntegerField()
	def __string__(self):
		return "%s" % (self.nama_tabel)

class PemisahanKata(models.Model):
    nama = models.CharField(max_length=50)
    kunciutama = models.CharField(max_length=15)
    kunciawal = models.CharField(max_length=15)
    kunciakhir = models.CharField(max_length=15) 
    deskripsi = models.TextField(blank=True,)
    jenis_data = models.CharField(max_length=50, blank=True)
    tanggal_buat = models.DateTimeField(auto_now_add=True)
    tanggal_edit = models.DateTimeField(blank=True)
	
    def __str__(self):
	    return "%s %s" % (self.nama, self.kunciutama)


class Kamus(models.Model):
	frasa = models.CharField(max_length=100)
	hasil = models.CharField(max_length=256, null=True)
	kategori_data = models.ForeignKey(KategoriData, on_delete=models.CASCADE, blank=True)
	keterangan = models.CharField(max_length=100)
    


class GrupData(models.Model):
    namadata = models.CharField(max_length=50)
    keterangan = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['namadata'], name='namadata')
    ]
    
    def __str__(self):
        return self.namadata


from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError
import os

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
lokasi = os.path.join(settings.MEDIA_ROOT, 'uploads')
lokasi2 = os.path.join(lokasi, 'users')
private_storage = FileSystemStorage(location= lokasi2)


Y="Ya"
T="Tidak"
YA_TIDAK = [(Y, 'Ya'), (T, 'Tidak')]


class Divisi(models.Model):
	divisi = models.CharField(max_length=50)
	keterangan = models.TextField(null=True)

	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['divisi'], name='divisi')
		]

	def __string__(self):
		return "%s" % (self.divisi)


class Pelanggan(models.Model):
	nama_pelanggan = models.CharField(max_length=50)
	alamat_pelanggan = models.CharField(max_length=256)
	hp_pelanggan = models.CharField(max_length = 13)
	email_pelanggan = models.EmailField()
	pkp = models.CharField(max_length=1, choices=YA_TIDAK, default=T)
	npwp_pelanggan  = models.CharField(max_length=20, null=True)
	jenis_pelanggan = models.IntegerField(default=0)
	divisi_pelanggan = models.ForeignKey(Divisi, on_delete=models.CASCADE, null=True)
	tanggal_buat = models.DateTimeField(auto_now_add=True, null="true")
	tanggal_edit = models.DateTimeField(blank=True, null="True")



class Suplier(models.Model):
	nama_suplier = models.CharField(max_length=50)
	alamat_suplier = models.CharField(max_length=256)
	hp_suplier = models.CharField(max_length = 13)
	email_suplier = models.EmailField()
	pkp = models.CharField(max_length=1, choices=YA_TIDAK, default=T)
	npwp_suplier  = models.CharField(max_length=20, null=True)
	divisi_suplier  = models.ForeignKey(Divisi, on_delete=models.CASCADE, null=True)
	tanggal_buat = models.DateTimeField(auto_now_add=True, null=True)
	tanggal_edit = models.DateTimeField(blank=True, null=True)


class Karyawan(models.Model):
	L="Laki-Laki"
	P="Perempuan"
	S="Single"
	W="Widow"
	M="Maried"

	JENIS_KELAMIN=[
        (L, 'Laki-Laki'),
        (P, 'Perempuan'),  
	]

	STATUS_PERKAWINAN=[
    	(S, 'Lajang'),
    	(W, 'Duda/Janda'),
    	(M, 'Kawin'),
	]
	
	nip = models.CharField(max_length=32, null=True, default="")
	nik = models.CharField(max_length=20)
	nama_karyawan = models.CharField(max_length=50)
	alias_karyawan = models.CharField(max_length=50)
	tp_lahir_karyawan = models.CharField(max_length=50)
	tg_lahir_karyawan = models.CharField(max_length=50)
	jn_kelamin_karyawan = models.CharField(max_length=1, choices = JENIS_KELAMIN, default = L,)
	status_karyawan = models.CharField(max_length=1, choices=STATUS_PERKAWINAN, default=S,)
	tanggungan_karyawan = models.IntegerField(null=True)
	alamat_karyawan = models.CharField(max_length=256)
	hp_karyawan = models.CharField(max_length = 13)
	jabatan_karyawan = models.CharField(max_length = 100 )
	tmt_masuk_karyawan = models.DateField(auto_now_add=True, null=True)
	email_karyawan = models.EmailField()
	divisi = models.ForeignKey(Divisi, on_delete=models.CASCADE, null=True)
	wajib_pajak = models.CharField(max_length=1, choices=YA_TIDAK, default=T)
	npwp_karyawan  = models.IntegerField()
	tanggal_buat = models.DateTimeField(auto_now_add=True, null=True)
	tanggal_edit = models.DateTimeField(blank=True, null=True)


class JenjangPendidikan(models.Model):
	jenjang = models.CharField(max_length=50)

	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['jenjang'], name='jenjang')
		]

	def __string__(self):
		return "%s" % (self.jenjang)


class Pendidikan(models.Model):
	nama = models.IntegerField()
	jenjang = models.ForeignKey(JenjangPendidikan, on_delete=models.CASCADE)
	jurusan = models.CharField(max_length=25)
	institusi = models.CharField(max_length=100)
	lulus = models.CharField(max_length=4)


class Kategori(models.Model):
	kategori = models.CharField(max_length=50)

	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['kategori'], name='kategori')
		]

	def __string__(self):
		return "%s" % (self.kategori)

class Brand(models.Model):
	brand = models.CharField(max_length=50, unique = True)

	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['brand'], name='brand')
		]

	def __string__(self):
		return "%s" % (self.brand)


class Produk(models.Model):
	kode_produk = models.CharField(max_length=100)
	barcode_produk = models.CharField(max_length=100, null=True)
	kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, default=0)
	nama_produk = models.CharField(max_length=50)
	suplier_produk = models.CharField(max_length=50)
	harga_produk = models.CharField(max_length=50)
	brand_produk = models.CharField(max_length=50)

	def __str__(self):
		return self.nama_produk	


class Uploads(models.Model):
    upload = models.FileField(storage=private_storage)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def filename(self):
    	return self.upload.path
    
    def __str__():
    	return "this path" 

class Photo(models.Model):
    file = models.ImageField()
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'    

class Jenjang(models.Model):
	pekerja = models.IntegerField(null=False)
	pendidikan = models.CharField(max_length=100)
	lulus = models.CharField(max_length=4)
	uploaded_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.pendidikan	

class HubunganKeluarga(models.Model):
	hubungan = models.CharField(max_length=50)

	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['hubungan'], name='hubungan')
		]
	def __str__(self):
		return self.hubungan

class Pekerjaan(models.Model):
	pekerjaan = models.CharField(max_length=50)
	uploaded_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['pekerjaan'], name='pekerjaan')
		]
	

	def __str__(self):
		return self.pekerjaan	

class Keluarga(models.Model):
	L="Laki-Laki"
	P="Perempuan"

	JENIS_KELAMIN=[
        (L, 'Laki-Laki'),
        (P, 'Perempuan'),  
	]	
	pekerja = models.IntegerField(default=0)
	nik = models.CharField(max_length=24)
	nama = models.CharField(max_length=100)
	tempat = models.CharField(max_length=100)
	tanggal = models.CharField(max_length=20)
	jenis = models.CharField(max_length=1, choices = JENIS_KELAMIN, default = L,)
	agama = models.CharField(max_length=15)
	pekerjaan = models.ForeignKey(Pekerjaan,on_delete=models.CASCADE)
	alamat = models.TextField(null=True)
	hubungan = models.ForeignKey(HubunganKeluarga,on_delete=models.CASCADE)
	telp = models.CharField(max_length=16, null=True)
	email = models.EmailField(null=True)
	status = models.IntegerField()
	uploaded_at = models.DateTimeField(auto_now_add=True)
    

class NonFormalList(models.Model):
	jenis = models.CharField(max_length=50)

	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['jenis'], name='jenis')
		]

	def __str__(self):
	    return self.jenis

class NonFormalPendidikan(models.Model):
	pekerja = models.IntegerField(null=False) ##hapus
	nosertifikat = models.CharField(max_length=100,null=True)
	jenis = models.ForeignKey(NonFormalList, on_delete=models.CASCADE)
	lembaga = models.CharField(max_length=100)
	jurusan = models.CharField(max_length=50)
	tahun = models.CharField(max_length=4)

	def __str__(self):
	    return self.lembaga		

class PengalamanKerja(models.Model):
	pekerja = models.IntegerField(null=False)
	perusahaan = models.CharField(max_length=100)
	alamat = models.CharField(max_length=100)
	usaha = models.CharField(max_length=50)
	posisi = models.CharField(max_length=50)
	alasan = models.CharField(max_length=100)
	thnawal = models.CharField(max_length=20)
	thnakhir = models.CharField(max_length=20)	

class JenjangKarir(models.Model):
	pekerja = models.IntegerField(null=False)
	divisi = models.CharField(max_length=100)
	jabatan = models.CharField(max_length=100)
	perusahaan = models.CharField(max_length=100)
	thnawal = models.CharField(max_length=20)
	thnakhir = models.CharField(max_length=20)		

class Kemampuan(models.Model):
	pekerja = models.IntegerField(null=False)
	kemampuan = models.CharField(max_length=100)
	tingkat = models.IntegerField()
	grade = models.CharField(max_length=20)
	serfikat = models.IntegerField()
	nosertifikat = models.CharField(max_length=100, null=True)
	tahun = models.CharField(max_length=20)
	status = models.IntegerField()

class Jabatan(models.Model):
	namajabatan = models.CharField(max_length=50)
	tingkat = models.IntegerField(null="True")
	upline = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['namajabatan'], name='namajabatan')
		] 

	def __str__(self):
		return self.namajabatan


class Pangkat(models.Model):
	pangkat = models.CharField(max_length=50)

	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['pangkat'], name='pangkat')
		]
	
	
	def __str__(self):
		return self.pangkat
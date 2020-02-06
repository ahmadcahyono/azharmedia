from django.contrib import admin

# Register your models here.
from master.models import (
	Suplier, 
	Pelanggan, 
	Karyawan,
	Produk,
	Brand,
	Pekerjaan,
	HubunganKeluarga,
	NonFormalList,
	NonFormalPendidikan,
	Jenjang, 
	Keluarga,
	PengalamanKerja,
	JenjangKarir,
	Kemampuan,
	Pendidikan,
	JenjangPendidikan,
	Pangkat,


)


admin.site.register(Suplier)
admin.site.register(Pelanggan)
admin.site.register(Karyawan)
admin.site.register(Produk)
admin.site.register(Brand)
admin.site.register(Jenjang)
admin.site.register(Pekerjaan)
admin.site.register(HubunganKeluarga)
admin.site.register(NonFormalList)
admin.site.register(NonFormalPendidikan)
admin.site.register(Keluarga)
admin.site.register(PengalamanKerja)
admin.site.register(JenjangKarir)
admin.site.register(Kemampuan)
admin.site.register(Pendidikan)
admin.site.register(JenjangPendidikan)
admin.site.register(Pangkat)
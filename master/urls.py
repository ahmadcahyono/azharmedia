from django.contrib import admin
from django.urls import path
from accounts import views as account_view 
from django.conf.urls import url
# from master.views import AmbilData, Topik
from master import views as master_view

app_name = 'data'

urlpatterns = [
	url(r'divisi/', master_view.divisi, name="divisi"),
	url(r'divisi_edit/(?P<update_id>[0-9]+)$', master_view.div_edit, name="divisi_edit"),
	url(r'divisi_delete/(?P<delete_id>[0-9]+)$', master_view.div_delete, name="divisi_delete"),

	url(r'^jenjangpendidikan/delete/(?P<delete_id>[0-9]+)$', master_view.jpendidikan_x,name="jpend_delete"),
 	url(r'^jenjangpendidikan/edit/(?P<update_id>[0-9]+)$', master_view.jpendidikan_e,name="jpend_edit"),
 	url(r'^jenjangpendidikan/', master_view.jenjangpendidikan,name="jenjangpendidikan"),

 	url(r'^hubungankeluarga/delete/(?P<delete_id>[0-9]+)$', master_view.hubungankeluarga_x,name="hubungankeluarga_delete"),
 	url(r'^hubungankeluarga/edit/(?P<update_id>[0-9]+)$', master_view.hubungankeluarga_e,name="hubungankeluarga_edit"),
 	url(r'^hubungankeluarga/', master_view.hubungankeluarga,name="hubungankeluarga"),

 	url(r'^pekerjaan/delete/(?P<delete_id>[0-9]+)$', master_view.pekerjaan_x,name="pekerjaan_delete"),
 	url(r'^pekerjaan/edit/(?P<update_id>[0-9]+)$', master_view.pekerjaan_e,name="pekerjaan_edit"),
 	url(r'^pekerjaan/', master_view.pekerjaan,name="pekerjaan"),


 	url(r'^pangkat/delete/(?P<delete_id>[0-9]+)$', master_view.pangkat_x,name="pangkat_delete"),
 	url(r'^pangkat/edit/(?P<update_id>[0-9]+)$', master_view.pangkat_e,name="pangkat_edit"),
 	url(r'pangkat/', master_view.pangkat,name="pangkat"),


 	url(r'^jabatan/delete/(?P<delete_id>[0-9]+)$', master_view.jabatan_x,name="jabatan_delete"),
 	url(r'^jabatan/edit/(?P<update_id>[0-9]+)$', master_view.jabatan_e,name="jabatan_edit"),
 	url(r'^jabatan/', master_view.jabatan,name="jabatan"),

 	url(r'^brand/delete/(?P<delete_id>[0-9]+)$', master_view.brand_x,name="brand_delete"),
 	url(r'^brand/edit/(?P<update_id>[0-9]+)$', master_view.brand_e,name="brand_edit"),
 	url(r'^brand/', master_view.brand,name="brand"),

 	url(r'^kategori/delete/(?P<delete_id>[0-9]+)$', master_view.kategori_x,name="kategori_delete"),
 	url(r'^kategori/edit/(?P<update_id>[0-9]+)$', master_view.kategori_e,name="kategori_edit"),
 	url(r'^kategori/', master_view.kategori,name="kategori"),

 	url(r'^nonformal/delete/(?P<delete_id>[0-9]+)$', master_view.nonformal_x,name="nonformal_delete"),
 	url(r'^nonformal/edit/(?P<update_id>[0-9]+)$', master_view.nonformal_e,name="nonformal_edit"),
 	url(r'^nonformal/', master_view.nonformal,name="nonformal"),


	url(r'^produk/', master_view.produk,name="produk"),
    url(r'^vendor/', master_view.vendor,name="vendor"),
    url(r'^pelanggan/', master_view.pelanggan,name="pelanggan"),
    url(r'^karyawan/', master_view.karyawan,name="karyawan"),
    url(r'^savephoto', master_view.savephoto,name="savephoto"),
]
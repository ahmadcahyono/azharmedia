from django.contrib import admin

from excels.models import (
	JenisData,
	KategoriData, 
	Kamus,
	GrupData, 
)


# Register your models here.
admin.site.register(JenisData)
admin.site.register(KategoriData)
admin.site.register(Kamus)

admin.site.register(GrupData)

from django.contrib import admin
from .models import (
	Module, 
	Menu, 
	App_Config,
	Provinsi,
	Kabupaten,
	Kecamatan,
	Kelurahan, 
)
# Register your models here.

admin.site.register(Module)
admin.site.register(Menu)
admin.site.register(App_Config)
admin.site.register(Provinsi)
admin.site.register(Kabupaten)
admin.site.register(Kecamatan)
admin.site.register(Kelurahan)
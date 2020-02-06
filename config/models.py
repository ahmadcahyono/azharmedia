from django.db import models

class Groups_access():
  	group_id = models.IntegerField()
  	module_id =  models.IntegerField()
  	access_data = models.TextField()

  	def __str__(self):
  		return self.access_data

class User_access():
  	user_id = models.IntegerField()
  	module_id =  models.IntegerField()
  	access_data = models.TextField()

  	def __str__(self):
  		return self.access_data


class Module(models.Model):
	M="master"
	R="report"
	P="proccess"
	C="core"
	G="generic"
	A="addon"

	MODUL_TIPE=[
       (M, 'master'),
       (R, 'report'),
       (P, 'proccess'),
       (C, 'core'),
       (G, 'generic'),
       (A, 'addon'),  
	]

	module_name = models.CharField(max_length=100)
	module_title = models.CharField(max_length=100)
	module_note = models.CharField(max_length=255)
	module_author = models.CharField(max_length=100)
	module_type = models.DateTimeField(auto_now_add=True)
	module_desc = models.TextField()
	module_db_key = models.CharField(max_length=100)
	module_type = models.CharField(max_length=1, choices=MODUL_TIPE, default=P,)
	module_config = models.TextField()
	module_lang = models.TextField()
	
	def __str__(self):
		return self.module_title


class Menu(models.Model):

	T='top'
	S='sidebar'
	B="both"

	MENU_POS=[(T,'top'),(S,'sidebar'),(B,'both'),]
	
	parent_id = models.IntegerField()
	module = models.IntegerField()
	url = models.CharField(max_length=100)
	menu_name = models.CharField(max_length=100)
	menu_type = models.CharField(max_length=10)
	role_id = models.CharField(max_length=100)
	deep =  models.IntegerField()
	ordering = models.IntegerField()
	position =  models.CharField(max_length=1, choices=MENU_POS, default=T) 
	#'top','sidebar','both') DEFAULT NULL,
	menu_icons = models.CharField(max_length=30)
	active =  models.IntegerField()
	access_data = models.TextField(),
	allow_guest = models.IntegerField(),
	menu_lang =  models.TextField()

	def __str__(self):
		return self.menu_name

class App_Config(models.Model
	):
	key = models.CharField(max_length=50, )
	value = models.CharField(max_length=500)

	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['key'], name='key')
		]

	def __str__(self):
		return self.value

class Jenis(models.Model):
	nama = models.CharField(max_length=50)
	
	def __str__(self):
		return self.nama

class Provinsi(models.Model):
	id_prov = models.CharField(max_length=2, unique=True)
	nama = models.CharField(max_length=100)
	def __str__(self):
		return self.nama

class Kecamatan(models.Model):
	id_kec = models.CharField(max_length=6, unique=True)
	id_kab = models.CharField(max_length=4)
	nama = models.CharField(max_length=100)

	def __str__(self):
		return self.nama


class Kelurahan(models.Model):
	id_kel = models.CharField(max_length=10, unique=True)
	id_kec = models.CharField(max_length=4)
	nama = models.CharField(max_length=100)
	jenis = models.IntegerField(default=0)

	def __str__(self):
		return self.nama

class Kabupaten(models.Model):
	id_kab = models.CharField(max_length=4, unique=True, default="")
	id_prop = models.CharField(max_length=2, null=True)
	nama = models.CharField(max_length=100, null=True)
	jenis = models.IntegerField(default=0)

	def __str__(self):
		return self.nama


class Log(models.Model):
	tanggal = models.DateTimeField(auto_now_add=True)
	user = models.IntegerField()
	ip = models.CharField(max_length=20)
	process = models.CharField(max_length=100)
	log_error = models.TextField()


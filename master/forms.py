from django import forms
from master.models import(
	Karyawan, Divisi, HubunganKeluarga, Pekerjaan, JenjangPendidikan,
	HubunganKeluarga, Brand, Kategori, Jabatan, NonFormalList, Pangkat,

)

class FormKaryawan(forms.ModelForm):
	class Meta:
		model = Karyawan
		fields = '__all__'
		widgets = {
			# 'karir' : forms.TextInput(={
			# 		'class' : 'form-control',
			# 		'placeholder' : 
			# 	}),
			
		}

class FormPangkat(forms.ModelForm):
	class Meta:
		model = Pangkat
		fields = '__all__'
		widgets = {
			'pangkat' : forms.TextInput(attrs={
				'class' : 'form-control',
				'placeholder' : 'Pangkat atau Golongan'

				}),
		}


class FormJenjangPendidikan(forms.ModelForm):
	class Meta:
		model = JenjangPendidikan
		fields = '__all__'
		widgets = {
			'jenjang' : forms.TextInput(attrs={
				'class' : 'form-control',
				'placeholder' : 'Jenjang pendidikan'

				}),
		}


class FormBrand(forms.ModelForm):
	class Meta:
		model = Brand
		fields = '__all__'
		widgets = {
			'brand' : forms.TextInput(attrs={
				'class' : 'form-control',
				'placeholder' : 'Brand atau merk barang'

				}),
		}

class FormKategori(forms.ModelForm):
	class Meta:
		model = Kategori
		fields = '__all__'
		widgets = {
			'kategori' : forms.TextInput(attrs={
				'class' : 'form-control',
				'placeholder' : 'Kategori Barang'

				}),
		}


class FormHubunganKeluarga(forms.ModelForm):
	class Meta:
		model = HubunganKeluarga
		fields = '__all__'
		widgets = {
			'hubungan' : forms.TextInput(attrs={
				'class' : 'form-control',
				'placeholder' : 'Hubungan Keluarga'

				}),
		}


class FormJabatan(forms.ModelForm):
	class Meta:
		model = Jabatan
		fields = '__all__'
		labels = {
			'namajabatan' : 'Jabatan',
			'tingkat' : 'Tingkat',
			'upline' : 'Bagian dari'
		}
		
		widgets = {
			'namajabatan' : forms.TextInput(attrs={
				'class' : 'form-control',
				'placeholder' : 'Nama jabatan'

				}),
			'tingkat' : forms.NumberInput(attrs={'class' : 'form-control', 'width' : 150}),
			'upline' : forms.Select(attrs={'class' : 'form-control'})
		}

	def __init__(self, *args, **kwargs):
		super(FormJabatan, self).__init__(*args, **kwargs)
		self.fields['upline'].queryset = Jabatan.objects.filter(tingkat=1)


class FormNonFormal(forms.ModelForm):
	class Meta:
		model = NonFormalList
		fields = '__all__'
		widgets = {
			'jenis' : forms.TextInput(attrs={
				'class' : 'form-control',
				}),
		}


class FormPekerjaan(forms.ModelForm):
	class Meta:
		model = Pekerjaan
		fields = '__all__'
		widgets = {
			'pekerjaan' : forms.TextInput(attrs={
				'class' : 'form-control',
				'placeholder' : 'Pekerjaan'

				}),
		}


class FormDivisi(forms.ModelForm):
	class Meta:
		model  = Divisi
		fields = '__all__'
		labels = {
			'divisi' : 'Nama Divisi',
			'keterangan' : 'Keterangan untuk divisi',

		}
		widgets = {
			'divisi' : forms.TextInput(
				attrs = {
					'class' : 'form-control',
					'placeholder' : 'nama divisi'
				}
			),

			'keterangan' : forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder' : 'keterangan dari divisi tersebut'
			})
		}



# def FormEksporData(forms.ModelForm):
# 	class Meta:
# 		model = Post
# 		fields = [
# 			'nama',
# 			'jenis',
# 			'alamat'
# 		]

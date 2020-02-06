from django import forms
from excels.models import JenisData

class FrmJenisData(forms.ModelForm):
	class Meta:
		model = JenisData
		fields = '__all__'
		
		labels = {
			'tabel_jd' : 'Tabel Sumber',
			'nama_jd' : 'Jenis Data',
			
		}
		
		widgets = {
			'nama_jd' : forms.TextInput(
				attrs={
					'class' : 'form-control',
					'placeholder' : 'jenis dari data'
				}
			),
			
			'tabel_jd' : forms.TextInput(
				attrs={
					'class' : 'form-control',
					'placeholder' : 'tabel'
				}
			),
		}

		error_messages = {
            'nama_jd': {
                'invalid': ("nama tersebut telah ada pada data"),
            },
        }

	def __init__(self, *args, **kwargs):
		super(FrmJenisData,self).__init__(*args, **kwargs)
		self.fields['nama_jd'].error_messages = {'required': 'Telah ada nama yang sama'}
		self.fields['nama_jd'].required = True
		self.fields['tabel_jd'].required = True 
		
	def clean(self):
	 	clean_data = super(FrmJenisData,self).clean()
	 	return clean_data
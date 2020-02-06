from django import forms

class FrmAppConfig(forms.ModelForm):
	class Meta:
		model = App_Config
		fields = '__all__'
		widgets = {
			'key' : forms.TextInput({
			 	'class' : 'form-control',
			 		'placeholder' : '',
			}),
			'value' : forms.TextInput({
				'class' : 'form-control',
			 		
			}),
			
		}
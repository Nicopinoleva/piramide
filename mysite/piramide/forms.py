from django import forms
from .models import Player

class CreateForm(forms.ModelForm):
	class Meta:
		model = Player
		fields = ['name']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'})
		}
from django import forms
from models import ThirdParty

class ThirdPartyForm(forms.ModelForm):

	class Meta:
		model = ThirdParty
		fields = ('name', 'description',)


from django import forms

from .models import User
from django.utils.translation import ugettext_lazy as _
import re

class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["firstName","lastName","phone","address"]
		widgets = {
			'firstName': forms.TextInput(attrs={'class':'form-control'}),
			'lastName': forms.TextInput(attrs={'class':'form-control'}),
			'phone': forms.TextInput(attrs={'class':'form-control'}),
			'address': forms.TextInput(attrs={'class':'form-control'}),
		}
		labels = {
			'firstName': _('First Name'),
			'lastName': _('Last Name'),
			'phone': _('Phone'),
			'address': _('Address'),
		}
		# help_texts = {
		# 	'firstName': _('Enter your First Name'),
		# }
		error_messages = {
			'firstName': {
				'max_length': _('First Name cant be too long'),
				'blank': _('First Name cant be blank'),
			}
		}

	def clean(self):
		first_name = self.cleaned_data.get("firstName")
		last_name = self.cleaned_data.get("lastName")
		phone = self.cleaned_data.get("phone")
		address = self.cleaned_data.get("address")

		if not first_name or not last_name or not phone or not address:
			raise forms.ValidationError("Fields cant be set blank")
		match = re.search("[^a-zA-Z]",first_name)
		if match:
			raise forms.ValidationError("Invalid First Name: Shouldn't contain any non-alphabetic characters")

		match = re.search("[^a-zA-Z]",last_name)
		if match:
			raise forms.ValidationError("Invalid Last Name: Shouldn't contain any non-alphabetic characters")
		
		match = re.search("[^\d]",phone)
		if match:
			raise forms.ValidationError("Invalid Phone Number")
		

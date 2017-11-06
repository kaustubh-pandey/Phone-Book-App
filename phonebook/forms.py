from django import forms
from .models import Phone
class AddNumber(forms.ModelForm):
	number=forms.CharField(label='Mobile Number')
	first_name=forms.CharField(label='First Name')
	last_name=forms.CharField(label='Last Name')
	email=forms.EmailField(label='Email')
	class Meta:
		model=Phone
		fields=['number','first_name','last_name','email']

class Number(forms.ModelForm):
	number=forms.CharField(label='Mobile Number')
	class Meta:
		model=Phone
		fields=['number']
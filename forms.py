from django import forms
from .models import StudentTBL

class StudentForm(forms.ModelForm):
	class  Meta:
		model = StudentTBL
		fields = [
		"RegistrationNumber",
		"Name",
		"FatherName",
		"DateOfBirth",
		"Contact",
		"Address",
		]
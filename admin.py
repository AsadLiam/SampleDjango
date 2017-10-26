from django.contrib import admin

#My new imports
from .models import StudentTBL

class Studentadmin(admin.ModelAdmin):
	list_display = (
		"RegistrationNumber",
		"Name",
		"FatherName",
		"DateOfBirth",
		"Contact",
		"Address",
		)
	search_fields = [
	"Name",
	"FatherName",
	]

# Register your models here.
admin.site.register(StudentTBL, Studentadmin)
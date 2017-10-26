from django.db import models

#My imports 
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save

# from .utils import unique_slug_generator

# Create your models here.

class StudentTBL(models.Model):
	GENDER_CHOICES = [
	("male", "Male"),
	("female","Female"),
	]
	RegistrationNumber = models.PositiveIntegerField(unique=0)
	Name = models.CharField(max_length=50)
	FatherName = models.CharField(max_length=50)
	gender = models.CharField(max_length = 7,
		choices=GENDER_CHOICES,
		default= "male"
		)
	clas = models.ForeignKey()
	slug = models.SlugField(unique=True)
	DateOfBirth = models.DateField(auto_now=False, auto_now_add=False)
	Contact = models.PositiveIntegerField()
	Address = models.CharField(max_length=100)

	def get_abs_url(self):
		return reverse("school:detail", kwargs={"slug": self.slug})
	
	def __str__(self):
		return str(self.Name)


class classez(model.Model):
	"""docstring for classz"""
	CLASS_CHOISE = (
		"Play Group",
		"Nercery",
		"Prep",
		"1st",
		"2nd",
		"3rd",
		"4th",
		"5th",
		"6th",
		"7th",
		"8th",
		"9th",
		"10th",
		)
	clas = models.CharField(max_length=10,
		choices=CLASS_CHOISE,
		default=""
		)
	def __str__(self):
		return str(self.clas)


def create_slug(instance, new_slug=None):
	slug = slugify(instance.Name)
	if new_slug is not None:
		slug = new_slug
	qs = StudentTBL.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug 



def pre_save_post_reciver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_reciver, sender=StudentTBL)
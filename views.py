from django.shortcuts import render, get_object_or_404, redirect

#My new imports
from .models import StudentTBL
from .forms import StudentForm
from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect
# Create your views here.

def list(request):
	stds = StudentTBL.objects.all()
	if not stds:
		raise Http404
	context = {
	"stds": stds,
	}
	return render(request, "school/list.html", context)

def create(request):
	if not request.user.is_authenticated():
		raise Http404
	form = StudentForm(request.POST)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request ,"Student has been added successfully!!")
		return HttpResponseRedirect("http://127.0.0.1:8000/school/")

	stds = StudentTBL.objects.all()
	context = {
	"form": form,
	"stds": stds,
	}
	return render(request, "school/create.html", context)

def read(request, slug=None):
	instance = get_object_or_404(StudentTBL, slug=slug)
	context = {
	"instance": instance,
	}
	return render(request, "school/read.html", context)

def update(request, slug=None):
	if not request.user.is_authenticated():
		raise Http404


	instance = get_object_or_404(StudentTBL, slug=slug)
	form = StudentForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Student is successfully updated")
		return HttpResponseRedirect(instance.get_abs_url())
	context = {
	"instance": instance,
	"form": form,
	}
	return render(request, "school/update.html", context)

def delete(request, slug=None):
	if not request.user.is_authenticated():
		raise Http404
	instance = get_object_or_404(StudentTBL, slug=slug)
	instance.delete()
	return redirect("school:list")
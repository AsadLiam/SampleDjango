from django.conf.urls import url

from . import views 

urlpatterns = [
	url(r'^$', views.list, name="list"),
	url(r'^create/$', views.create, name="create"),
	url(r'^(?P<slug>[\w-]+)/$', views.read, name="detail"),
	url(r'^(?P<slug>[\w-]+)/edit/$', views.update, name="update"),
	url(r'^(?P<slug>[\w-]+)/delete/$', views.delete, name="delete"),
	# url(r'^(?P<student_id>\d+)/')
]



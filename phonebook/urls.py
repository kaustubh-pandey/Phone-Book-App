from django.conf.urls import url
from . import views
from .views import *
app_name='phonebook'

urlpatterns=[
	url(r'^$', views.index, name='index'),
	url(r'^add/$',views.addNumber,name='add'),
	url(r'^search/$',views.search,name='search'),
]

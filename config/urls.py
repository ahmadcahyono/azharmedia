from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from config import views as config_view

app_name = 'konfig'

urlpatterns = [
	url(r'^setup/', config_view.index, name='setup'),

]

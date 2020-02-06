from django.contrib import admin
from django.urls import path
from excels import views as excel_view
from accounts import views as account_view 
from django.conf.urls import url
# from excels.views import AmbilData, Topik

app_name = 'proses'

urlpatterns = [
 	url(r'^jd', excel_view.getjenisdata,name="jd"),
 	url(r'^jenisdata', excel_view.jenisdata,name="jenisdata"),
 	url(r'^edit_jdata/(?P<update_id>[0-9]+)$', excel_view.edit_jenisdata,name="edit_jdata"),
 	url(r'^delete_jdata/(?P<delete_id>[0-9]+)$', excel_view.delete_jenisdata,name="delete_jdata"),
    
    url(r'^loadxls', excel_view.load_excel,name="laodxls"),
 	

    url(r'^searchbasic/', excel_view.criteria,name="searchbasic"),
    url(r'^searchsetting/', excel_view.kalimat,name="searchsetting"),
    url(r'^dataprocess/', excel_view.dataprocess,name="dataprocess"),



	# url(r'^$', AmbilData.as_view(), name="home"),
	# # url(r'^savephoto/', excel_view.savephoto, name='savephoto'),
	# url(r'simkar/', excel_view.simkar, name="simkar"),
	
]
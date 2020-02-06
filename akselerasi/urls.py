from django.contrib import admin
from django.urls import path, include
from excels import views as excel_view
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as account_view 
from django.conf.urls import url

urlpatterns = [
    
    path('admin/', admin.site.urls),
    url(r'^$', excel_view.index, name="index"),
    
    url(r'^login/', account_view.user_login, name="login"),
    url(r'^logout/', account_view.user_logout, name="logout"),
    url(r'^lockscr/', account_view.user_lockscr, name="lockscr"),
    url(r'^recoverpw/', account_view.user_recoverpw, name="recoverpw"),
    url(r'^register/', account_view.user_register, name="register"),
    
    url(r'^konfig/', include(('config.urls'),namespace="konfig")),
    
    url(r'^data/', include(('master.urls'),namespace="data")),
    url(r'^proses/', include(('excels.urls'),namespace="proses")),
    # url(r'^divisi/', excel_view.divisi,name="divisi"),
    # url(r'^divisi/', excel_view.divisi,name="divisi"),
    
    
    url(r'^ubahtable/', excel_view.gantitabel,name="gantitabel"),
    url(r'^dt/(?P<table>\w+)', excel_view.getdata,name="dt"),
    
    
    # url(r'^ambil/', include(('excels.urls', 'ambil'),namespace="ambil")), 
    # # url(r'^uji/', excel_view.uji,name="uji"),
    # url(r'^blank/', excel_view.blank,name="blank"),
    # url(r'^indeks/', excel_view.indeks,name="indeks"),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

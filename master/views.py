from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.forms.models import model_to_dict
import django.http
from django.core import serializers
from django.db.models import F
from django.forms.models import model_to_dict
from django.core.files.base import ContentFile
from master.forms import (
  FormDivisi,
  FormBrand,
  FormPangkat,
  FormJenjangPendidikan,
  FormKategori,
  FormHubunganKeluarga,
  FormJabatan,
  FormNonFormal,
  FormPekerjaan,
)

from master.models import (
    Divisi,
    Photo as foto,
    Uploads as photo, 
    Pelanggan, 
    Suplier, 
    Karyawan,
    Pekerjaan, 
    Produk,
    JenjangPendidikan,
    HubunganKeluarga,
    NonFormalList,
    Brand,
    Kategori, Jabatan,
    Pangkat,
)
import uuid
import base64

from base64 import decodestring


from config.models import (
     Kabupaten as kab,
)

from django.views import View
from base64 import b64encode, b64decode


from django.views.generic.base import (
    RedirectView, 
    TemplateView,
    # View,
)
# Create your views here.

@login_required
def kategori(request):
  data = dict()
  kategori = Kategori.objects.all()
  kategori_form = FormKategori(request.POST or None)
  if request.method == 'POST':
    if kategori_form.is_valid():
      kategori_form.save()
      kategori_form = FormKategori()
      data = {
        'form_kategori' : kategori_form,
        'kategori' : kategori,
        'tombol' : 'Simpan',
        'pesan' : 'Buat Data Baru',
      }
  else:
    data = {
      'form_kategori' : kategori_form,
      'kategori' : kategori,
      'tombol' : 'Simpan',
      'pesan' : 'Buat Data Baru',
    }

  return render(request, 'masterdata/pages/kategori.html', data)


@login_required
def kategori_e(request, update_id):
  kategori_edit = Kategori.objects.get(id=update_id)
  kategori = Kategori.objects.all()
  data = dict()
  mydata = {
    'kategori' : kategori_edit.kategori,
  }
  kategori_form = FormKategori(request.POST or None, initial=mydata, instance=kategori_edit)
  if request.method == 'POST':
    if kategori_form.is_valid():
      kategori_form.save()
      return redirect('data:kategori')
  else:
    data = {
        'kategori' : kategori, 
        'form_kategori' : kategori_form, 
        'tombol' : 'Edit',
        'pesan' : 'Merubah Data',
      }  

  return render(request, 'masterdata/pages/kategori.html', data)


@login_required
def kategori_x(request, delete_id):
    divisi = Kategori.objects.filter(id=delete_id).delete()
    return redirect('data:kategori')


@login_required
def brand(request):
  brand = Brand.objects.all()
  form = FormBrand(request.POST or None)
  data = {}
  if request.method == 'POST':
    if form.is_valid():
      form.save()
      brand = Brand.objects.all()
      form = FormBrand()
      data = {
        'brands' : brand, 
        'form_brand' : form, 
        'tombol' : 'Simpan',
        'pesan' : 'Data berhasil disimpan',
      }
  else:
    data = {
        'brands' : brand, 
        'form_brand' : form, 
        'tombol' : 'Simpan',
        'pesan' : 'Penambahan data',
      }
  return render(request, 'masterdata/pages/brand.html', data)


@login_required
def brand_e(request, update_id):
  brand_update = Brand.objects.get(id=update_id)
  data = {}
  mydata = {
    'brand' : brand_update.brand,
  }
  form = FormBrand(request.POST or None, initial=data, instance=brand_update)
  if request.method=='POST':
    if form.is_valid():
      form.save()
      return redirect('data:brand')
  else:
    brand = Brand.objects.all()
    data = {
      'brands' : brand, 
      'form_brand' : form, 
      'tombol' : 'Edit',
      'pesan' : 'Edit Data',
    }
  return render(request, 'masterdata/pages/brand.html', data)
  

@login_required
def brand_x(request, delete_id):
    divisi = Brand.objects.filter(id=delete_id).delete()
    return redirect('data:brand')


@login_required
def pangkat(request):
  pangkat = Pangkat.objects.all()
  form_pangkat = FormPangkat(request.POST or None)
  data = {}
  if request.method == 'POST':
    if form_pangkat.is_valid():
      form_pangkat.save()
      pangkat = Pangkat.objects.all()
      form_pangkat = FormPangkat()
      data = {
        'title' : 'Data Karir',
        'pangkat' : pangkat,
        'form_pangkat' : form_pangkat,
        'tombol' : 'Simpan',
        'pesan' : 'Buat Data Baru',    
      }
  else:
    # form_pangkat = FormPangkat() 
    data = {
      'title' : 'Daftar Pangkat',
      'pangkat' : pangkat,
      'form_pangkat' : form_pangkat,
      'tombol' : 'Simpan',
      'pesan' : 'Buat Data Baru',    
    }

  return render(request, 'masterdata/pages/pangkat.html', data)


@login_required
def pangkat_e(request, update_id):
  pangkat_update = Pangkat.objects.get(id=update_id)
  pangkat = Pangkat.objects.all()
  datalist = dict()
  data = {
    'pangkat' : pangkat_update.pangkat,

  }
  pangkat_form = FormPangkat(request.POST or None, initial=data, instance=pangkat_update)
  if request.method == 'POST' :
    if pangkat_form.is_valid():
      pangkat_form.save()
      return redirect('data:pangkat')
  else:
    datalist = {
        'title' : 'Daftar Pangkat',
        'pangkat' : pangkat,
        'form_pangkat' : pangkat_form,
        'tombol' : 'Edit',
        'pesan' : 'Pembaharuan data',    

      }
  return render(request, 'masterdata/pages/pangkat.html', datalist)
  

@login_required
def pangkat_x(request, delete_id):
    divisi = Pangkat.objects.filter(id=delete_id).delete()
    return redirect('data:pangkat')
   # return render(request, 'masterdata/pages/pendidikan.html')


@login_required
def hubungankeluarga(request):
  hubungan = HubunganKeluarga.objects.all()
  form_hubungan = FormHubunganKeluarga(request.POST or None)
  datalist = {}
  if request.method == 'POST':
    if form_hubungan.is_valid():
      form_hubungan.save()
      hubungan = HubunganKeluarga.objects.all()
      form_hubungan = FormHubunganKeluarga()
      datalist = {
        'title' : 'Daftar Hubungan Keluarga',
        'hubungan' : hubungan,
        'form_hubungan' : form_hubungan,
        'tombol' : 'Simpan',
        'pesan' : 'Daftar berhasil ditambahkan',      
      }
  else:    
    datalist = {
      'title' : 'Daftar Hubungan Keluarga',
      'hubungan' : hubungan,
      'form_hubungan' : form_hubungan,
      'tombol' : 'Simpan',
      'pesan' : 'Tambah daftar',      
    }
  return render(request, 'masterdata/pages/hubungan.html', datalist)


@login_required
def hubungankeluarga_e(request, update_id):
  hubungan_update = HubunganKeluarga.objects.get(id=update_id)
  data = {'hubungan' : hubungan_update.hubungan}
  form_hubungan = FormHubunganKeluarga(request.POST or None, initial = data, instance=hubungan_update)
  datalist =  {} 
  if request.method == 'POST':
    if form_hubungan.is_valid():
      form_hubungan.save()
      return redirect('data:hubungankeluarga')
  else:
    hubungan = HubunganKeluarga.objects.all()
    datalist = {
        'title' : 'Daftar Hubungan Keluarga',
        'hubungan' : hubungan,
        'form_hubungan' : form_hubungan,
        'tombol' : 'Edit',
        'pesan' : 'perbaharuan data',      
    }
  return render(request, 'masterdata/pages/hubungan.html',datalist)

@login_required
def hubungankeluarga_x(request, delete_id):
    divisi = Karir.objects.filter(id=delete_id).delete()
    return redirect('data:hubungankeluarga')


@login_required
def pekerjaan(request):
  form_pekerjaan = FormPekerjaan(request.POST or None)
  pekerjaan = Pekerjaan.objects.all()
  data = {}
  if request.method == 'POST':
    if form_pekerjaan.is_valid():
      form_pekerjaan.save()
      pekerjaan = Pekerjaan.objects.all()
      form_pekerjaan = FormPekerjaan()
      data = {
        'title' : 'Daftar Pekerjaan',
        'pekerjaan' : pekerjaan,
        'form_pekerjaan' : form_pekerjaan,
        'tombol' : 'Simpan',
        'pesan' : 'Daftar ditambahkan',      
      }  
  else:    
    data = {
        'title' : 'Daftar Pekerjaan',
        'pekerjaan' : pekerjaan,
        'form_pekerjaan' : form_pekerjaan,
        'tombol' : 'Simpan',
        'pesan' : 'Buat daftar baru',      
    }
  return render(request, 'masterdata/pages/pekerjaan.html', data)


@login_required
def pekerjaan_e(request, update_id):
  pekerjaan_update = Pekerjaan.objects.get(id=update_id)
  data = {
    'pekerjaan' : pekerjaan_update.pekerjaan,
  }
  datalist = {}
  form_pekerjaan = FormPekerjaan(request.POST or None, initial = data, instance=pekerjaan_update)
  if request.method == 'POST' :
    if form_pekerjaan.is_valid():
      form_pekerjaan.save()
      return redirect('data:pekerjaan')
  else:
    pekerjaan = Pekerjaan.objects.all()
    datalist = {
        'title' : 'Daftar Pekerjaan',
        'pekerjaan' : pekerjaan,
        'form_pekerjaan' : form_pekerjaan,
        'tombol' : 'Edit',
        'pesan' : 'Perbaharuan data',       
      }

  return render(request, 'masterdata/pages/pekerjaan.html', datalist)

@login_required
def pekerjaan_x(request, delete_id):
    divisi = Pekerjaan.objects.filter(id=delete_id).delete()
    return redirect('data:pekerjaan')


@login_required
def jabatan(request):
  dataku = {}
  jabatan = Jabatan.objects.all()
  form_jabatan = FormJabatan(request.POST or None)
  nilai = 1
  if request.method == 'POST':
    if form_jabatan.is_valid():
      form_jabatan.save()
      jabatan = Jabatan.objects.all()
      form_jabatan = FormJabatan()
      dataku = {
        'title' : 'Daftar Jabatan', 
        'form_jabatan' : form_jabatan,
        'jabatan' : jabatan,
        'tombol' : 'Simpan',
        'pesan' : 'daftar berhasil ditambah',
        'nilai' : nilai,
      }    
  else:
    dataku = {
        'title' : 'Daftar Jabatan', 
        'form_jabatan' : form_jabatan,
        'jabatan' : jabatan,
        'tombol' : 'Simpan',
        'pesan' : 'Penambahan daftar',
        'nilai' : nilai,
    }
  return render(request, 'masterdata/pages/jabatan.html', dataku)


@login_required
def jabatan_e(request, update_id):
  jabatan_update = Jabatan.objects.get(id=update_id)
  data = {
    'namajabatan' : jabatan_update.namajabatan, 
    'tingkat' : jabatan_update.tingkat,
    'upline' : jabatan_update.upline,
  }
  form_jabatan = FormJabatan(request.POST or None, initial=data, instance=jabatan_update)
  if request.method == 'POST':
    if form_jabatan.is_valid():
      form_jabatan.save()  
      return redirect('data:jabatan')
  
  jabatan = Jabatan.objects.all()
  dataku = {
    'title' : 'Daftar Jabatan', 
    'form_jabatan' : form_jabatan,
    'jabatan' : jabatan,
    'tombol' : 'Edit',
    'pesan' : 'Perbaharuan data',
  }  
  return render(request, 'masterdata/pages/jabatan.html', dataku)

@login_required
def jabatan_x(request, delete_id):
    divisi = Karir.objects.filter(id=delete_id).delete()
    return redirect('data:jabatan')



@login_required
def jenjangpendidikan(request):
  jenjang = JenjangPendidikan.objects.all()
  form_jenjang = FormJenjangPendidikan(request.POST or None)
  data = {}
  if request.method == 'POST':
    if form_jenjang.is_valid():
      form_jenjang.save()
      form_jenjang = FormJenjangPendidikan()
      jenjang = JenjangPendidikan.objects.all()
      data = {
        'title' : 'Daftar Jenjang Pendidikan Formal',
        'jenjang' : jenjang,
        'form_jenjang' : form_jenjang,
        'tombol' : 'Simpan',
        'pesan' : 'Penambahan data berhasil'
      }
  else:
    data = {
        'title' : 'Daftar Jenjang Pendidikan Formal',
        'jenjang' : jenjang,
        'form_jenjang' : form_jenjang,
        'tombol' : 'Simpan',
        'pesan' : 'Penambahan data baru'
     }
  return render(request, 'masterdata/pages/jenjangpendidikan.html', data)


@login_required
def jpendidikan_e(request, update_id):
  jenjang_update = JenjangPendidikan.objects.get(id=update_id)
  data = {'jenjang' : jenjang_update.jenjang,}
  form_jenjang = FormJenjangPendidikan(request.POST or None, initial=data, instance=jenjang_update)
  if request.method == 'POST':
    if form_jenjang.is_valid():
      form_jenjang.save()
      return redirect('data:jenjangpendidikan')
  jenjang = JenjangPendidikan.objects.all()
  data = {
    'title' : 'Edit Jenjang Pendidikan',
    'jenjang' : jenjang,
    'form_jenjang' : form_jenjang,
    'tombol' : 'Edit',
    'pesan' : 'Update Jenjang Pendidikan',
  }
  return render(request, 'masterdata/pages/jenjangpendidikan.html', data)

@login_required
def jpendidikan_x(request, delete_id):
    divisi = JenjangPendidikan.objects.filter(id=delete_id).delete()
    return redirect('data:jenjangpendidikan')
   # return render(request, 'masterdata/pages/pendidikan.html')

@login_required
def nonformal(request):
  nonformal = NonFormalList.objects.all()
  form_nonformal = FormNonFormal(request.POST or None)
  data = {}
  if request.method == 'POST' : 
    if form_nonformal.is_valid():
      form_nonformal.save()
      form_nonformal = FormNonFormal()
      nonformal = NonFormalList.objects.all()
      data =  {
       'title':'Daftar Pendidikan Non Formal',
       'nonformal': nonformal,
       'form_nonformal' : form_nonformal,
       'tombol' : 'Simpan',
       'pesan' : 'Daftar berhasil ditambahkan'
      }
  else:
    data =  {
       'title':'Daftar Pendidikan Non Formal',
       'nonformal': nonformal,
       'form_nonformal' : form_nonformal,
       'tombol' : 'Simpan',
       'pesan' : 'Tambah daftar'
      }
  
  return render(request, 'masterdata/pages/nonformal.html', data)

@login_required
def nonformal_e(request, update_id):
  nonformal_update = NonFormalList.objects.get(id=update_id)
  data = {'jenis' : nonformal_update.jenis}
  form_nonformal = FormNonFormal(request.POST or None, initial=data, instance=nonformal_update)
  if request.method == 'POST' : 
    if form_nonformal.is_valid():
      form_nonformal.save()
      return redirect('data:nonformal')

  nonformal = NonFormalList.objects.all()
  data = {
   'title' : 'Daftar Pendidikan Non Formal',
   'nonformal' : nonformal,
   'form_nonformal' : form_nonformal,
   'tombol' : 'Edit',
   'pesan' : 'Perbaharuan data'
  }

  return render(request, 'masterdata/pages/nonformal.html', data)

@login_required
def nonformal_x(request, delete_id):
  data = NonFormalList.objects.filter(id=delete_id).delete()
  return redirect('data:nonformal')

@login_required
def vendor(request):
   return render(request, 'masterdata/pages/vendor.html')
   return redirect('data:nonformal')

@login_required
def div_delete(request, delete_id):
  divisi_delete = Divisi.objects.filter(id=delete_id).delete()
  return redirect('data:divisi')




@login_required
def div_edit(request, update_id):
  divisi_update = Divisi.objects.get(id=update_id)
  divisi = Divisi.objects.all()
  
  data = {
    'divisi' : divisi_update.divisi,
    'keterangan' : divisi_update.keterangan,
  }

  form_divisi = FormDivisi(request.POST or None, initial=data, instance=divisi_update)
  
  if request.method == 'POST':
    if form_divisi.is_valid():
      form_divisi.save()
      return redirect('data:divisi')
  else:
      context = {
      'title' : 'Update Divisi',
      'divisi' : divisi,
      'form_divisi' : form_divisi,
      'tombol' : 'Edit',
      'pesan' : 'Data belum terupdate',

      }

  return render(request, 'masterdata/pages/divisi.html', context)


@login_required
def divisi(request):
  divisi = Divisi.objects.all()
  divisi_form = FormDivisi(request.POST or None)
  if request.method == 'POST':
    if divisi_form.is_valid():
        divisi_form.save()
        divisi = Divisi.objects.all()
        divisi_form = FormDivisi()
        context = {
          'title' : 'Divisi',
          'divisi' : divisi,
          'form_divisi' : divisi_form,
          'tombol' : 'Simpan',
          'pesan' : 'Data berhasil disimpan',
        }
  else :
    divisi_form = FormDivisi()
    context = {
      'title' : 'Divisi',
      'divisi' : divisi,
      'form_divisi' : divisi_form,
      'tombol' : 'Simpan',
      'pesan' : 'Membuat data baru',

    }
    
  return render(request, 'masterdata/pages/divisi.html', context)  


@login_required
def pelanggan(request):
   return render(request, 'masterdata/pages/pelanggan.html')

@login_required
def karyawan(request):
  from datetime import datetime
   # bulan = dict()
  tanggal = range(1,32)
  

  tahun = range(1980, (datetime.today().year+1))
  rtahun = range(datetime.today().year+1 , 1980-1, -1)
  tgl_sekarang = datetime.today().day
  bln_sekarang = datetime.today().month
  bulan = {
      1:'Januari',
      2:'Februari',
      3:'Maret',
      4:'April',
      5:'Mei',
      6:'Juni',
      7:'Juli',
      8:'Agustus',
      9:'September',
      10:'Oktober',
      11:'Nopember',
      12:'Desember',
   }
  nama_bln = bulan[bln_sekarang]
  thn_sekarang = datetime.today().year
  list_kab = kab.objects.all().values('nama')
  bulan2 = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','Nopember','Desember',]
  pendidikan = JenjangPendidikan.objects.all().values('jenjang')
  nonformal = NonFormalList.objects.all().values('jenis')
  pangkat = Pangkat.objects.all()
  jabatan = Jabatan.objects.all()
  hkeluarga = HubunganKeluarga.objects.all()
  return render(request, 'masterdata/pages/karyawan.html',
    { 
      'sekarang' :thn_sekarang,
      'nama_bln' : nama_bln,
      'tgl' : tgl_sekarang,
      'bulan': bulan,
      'tanggal': tanggal,
      'tahun' : tahun,
      'rtahun' : rtahun, 
      'bulan2' : bulan2, 'kab' : list_kab,
      'pendidikan' : pendidikan,
      'nf' : nonformal,
      'hubkeluarga' : hkeluarga,
      'pangkat' : pangkat,
      'jabatan' : jabatan, 
    }
  )



@login_required
def produk(request):
   return render(request, 'masterdata/pages/produk.html')




@login_required(login_url='/login/')
def get_folder(request):
    path = dict()
    path['respon'] = "salah"
    return JsonResponse(path)


def databaseku(mydata):
    dataku = {}
    if(mydata.lower()=="agen"):
      mode='Agen'
      dataku1 = Pelanggan.objects.all().annotate(nama=F('nama_pelanggan'))
      dataku = Pelanggan.objects.all().values('id', 'nama_pelanggan').annotate(nama=F('nama_pelanggan'))
    elif(mydata.lower()=="suplier"):
      mode='Suplier'
      dataku = Suplier.objects.all().annotate(nama=F('nama_suplier'))
    elif(mydata.lower()=="bank"):
      mode='Bank'
      dataku = Kamus.objects.all().annotate(nama=F('frasa'))
    elif(mydata.lower()=="karyawan"):
      mode='Karyawan'
      dataku = Karyawan.objects.all().annotate(nama=F('nama_karyawan'))
    elif(mydata.lower()=="produk"):
      mode='Produk'
      dataku = Produk.objects.all().annotate(nama=F('nama_produk'))
    return dataku



@csrf_exempt
def gantitabel(request):
    dataku = {}
    dataku1 = dict()
    mode = ''
    if request.method == "POST":
      
      mydata = request.POST.get('asing')
      dataku = databaseku(mydata)
      # ser_obj = serializers.serialize('json', dataku)
      # struct = json.loads(ser_obj)
      # data = json.dumps(struct)
      
      baris = list()
      

      for isi in dataku:
        baris.append((isi['id'],  isi['nama']))
      hasilnya = json.dumps(baris)
      print(hasilnya)
      return HttpResponse(hasilnya, content_type='application/json')


"""
Came up with this for satchmo's downloadable product migration, 0001_split.
"""
def db_table_exists(table, cursor=None):
    from django.db import connection
    return table in connection.introspection.table_names()


@csrf_exempt
def getdata(request,table):
  dataku = {}
  baris = list()
  store = table.title()
  print(store)
  dataku = databaseku(table)
  for isi in dataku:
        baris.append((isi['id'],  isi['nama']))
      
  tamp = "masterdatas_" + table
  hasil = db_table_exists(tamp)
  data = json.dumps(baris)
      
  # sadino = {'nama' : hasil, 'v' : vasa}
  return HttpResponse(data , content_type='applcation/json')



class CSRFExemptMixin(object):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CSRFExemptMixin, self).dispatch(request, *args, **kwargs)



@csrf_exempt
def getjenisdata(request):
  dataku = {}
  baris = list()
  dataku = JenisData.objects.all().values('id', 'nama_jd');
  
  for isi in dataku:
        baris.append((isi['id'],  isi['nama_jd']))
  # sadino = {'nama' : hasil, 'v' : vasa}
  data = json.dumps(baris)
  return HttpResponse(data , content_type='application/json')




def photo_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'album/photo_list.html', {'form': form, 'photos': photos})


@csrf_exempt
def savephoto(request):
  import datetime
  now = datetime.datetime.now()
  width = 600
  height = 400 
  result = dict()
  if request.is_ajax():
    imagen1 = request.POST.get('gambar')
    ext = request.POST.get('ext')
    nkar = request.POST.get('nip')
    image_data = imagen1.replace('data:image/' + ext + ';base64,','')
    image_name = nkar + "_" + str(uuid.uuid4())+"."+ ext
    gambar = base64.b64decode(image_data)
    dara = ContentFile(gambar)
    citra = photo()
    citra.upload.save(image_name,dara)
    c = photo.objects.latest('pk')
    result['pk'] = c.pk
    result['file'] = image_name
    result['status'] = 'upload berhasil'
    status = c.pk
    
  else:
    result['pk'] = ''
    result['file'] = ''
    result['status'] = 'upload gagal'
    # status = 'upload gagal'

  return JsonResponse(result, safe=False)
  

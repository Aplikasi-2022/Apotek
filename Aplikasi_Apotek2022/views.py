from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Model_kategori, Model_satuan, Model_suplier, Model_obat, Model_kadaluarsa, Model_pembelian, Model_penjualan1
import hashlib

def index(request):
	context = {
	'page_title':'Login',
	}
	#print(request.user)
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('Home')
		else:
			return redirect('index')

	return render(request, 'login.html',  context)

def HomeView(request):	
	context = {
	'page_title':'Home'
	}
	return render(request, 'home.html',  context)

def LogoutView(request):
	context = {
	'page_title':'logout',
	}
	if request.method == "POST":
		if request.POST["logout"] == "Submit":	
			logout(request)

		return redirect('index')

	return render(request, 'logout.html',  context)	

# data kategori
def Data_kategori(request):	
	data = Model_kategori.objects.all()
	context = {
	'page_title':'Tabel',
	'data': data,
	}
	return render(request, 'Master_data/data_kategori/tabel.html',  context)

def Tambah_kategori(request):
	kode = Model_kategori.objects.count()
	kode_otomatis = kode + 1;
	if request.method == 'POST':
		Model_kategori.objects.create(
			kode_kategori = request.POST['kode_kategori'],
			nama_kategori = request.POST['nama_kategori'],
			harga = request.POST['harga'],
			gambar = request.FILES['gambar'],
			keterangan = request.POST['keterangan'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/kategori/")		
	context = {	
	'Tambah_kategori':'Tambah_kategori',
	'kode_otomatis': kode_otomatis,
	}
	return render(request, 'Master_data/data_kategori/tambah.html',  context)

def Hapus_kategori(request, hapus_k):
	Model_kategori.objects.filter(id=hapus_k).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('kategori')

def Edit_kategori(request, id_k):		
	edit_data = Model_kategori.objects.get(id=id_k)
	if request.method == 'POST':		
			edit_data.kode_kategori = request.POST.get('kode_kategori')
			edit_data.nama_kategori = request.POST.get('nama_kategori')
			edit_data.harga = request.POST.get('harga')
			edit_data.gambar = request.FILES.get('gambar')
			edit_data.keterangan = request.POST.get('keterangan')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('kategori')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_kategori/edit.html',  context)	

# data satuan
def Data_satuan(request):	
	data = Model_satuan.objects.all()
	context = {
	'page_title':'Tabel',
	'data': data,
	}
	return render(request, 'Master_data/data_satuan/tabel.html',  context)

def Tambah_satuan(request):
	kode = Model_satuan.objects.count()
	kode_otomatis = kode + 1 ;
	if request.method == 'POST':
		Model_satuan.objects.create(
			kode_satuan = request.POST['kode_satuan'],
			nama_satuan = request.POST['nama_satuan'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/satuan/")		
	context = {	
	'Tambah_satuan':'Tambah_satuan',
	'kode_otomatis': kode_otomatis,
	}
	return render(request, 'Master_data/data_satuan/tambah.html',  context)

def Hapus_satuan(request, hapus_s):
	Model_satuan.objects.filter(id=hapus_s).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('satuan')

def Edit_satuan(request, id_s):		
	edit_data = Model_satuan.objects.get(id=id_s)
	if request.method == 'POST':		
			edit_data.kode_satuan = request.POST.get('kode_satuan')
			edit_data.nama_satuan = request.POST.get('nama_satuan')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('satuan')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_satuan/edit.html',  context)	

# data suplier
def Data_suplier(request):	
	data = Model_suplier.objects.all()
	context = {
	'page_title':'Tabel',
	'data': data,
	}
	return render(request, 'Master_data/data_suplier/tabel.html',  context)

def Tambah_suplier(request):
	kode = Model_suplier.objects.count()
	kode_otomatis = kode + 1;
	if request.method == 'POST':
		Model_suplier.objects.create(
			kode_suplier = request.POST['kode_suplier'],
			nama_suplier = request.POST['nama_suplier'],
			lokasi = request.POST['lokasi'],
			telp = request.POST['telp'],
			email = request.POST['email'],
			alamat = request.POST['alamat'],			
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/suplier/")		
	context = {	
	'Tambah_suplier':'Tambah_suplier',
	'kode_otomatis': kode_otomatis,
	}
	return render(request, 'Master_data/data_suplier/tambah.html',  context)

def Hapus_suplier(request, hapus_sp):
	Model_suplier.objects.filter(id=hapus_sp).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('suplier')

def Edit_suplier(request, id_sp):		
	edit_data = Model_suplier.objects.get(id=id_sp)
	if request.method == 'POST':		
			edit_data.kode_suplier = request.POST.get('kode_suplier')
			edit_data.nama_suplier = request.POST.get('nama_suplier')
			edit_data.lokasi = request.POST.get('lokasi')
			edit_data.telp = request.POST.get('telp')
			edit_data.email = request.POST.get('email')
			edit_data.alamat = request.POST.get('alamat')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('suplier')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_suplier/edit.html',  context)

# data obat
def Data_obat(request):	
	data = Model_obat.objects.all()
	context = {
	'page_title':'Tabel',
	'data': data,
	}
	return render(request, 'Master_data/data_obat/tabel.html',  context)

def Tambah_obat(request):
	kode_otomatis = Model_obat.objects.count()
	kode = kode_otomatis + 1;
	select_suplier = Model_suplier.objects.all()
	select_kategori = Model_kategori.objects.all()
	select_satuan = Model_satuan.objects.all()
	if request.method == 'POST':
		Model_obat.objects.create(
			kode_obat = request.POST['kode_obat'],
			nama_obat = request.POST['nama_obat'],
			nama_suplier = request.POST['nama_suplier'],
			nama_kategori = request.POST['nama_kategori'],
			nama_satuan = request.POST['nama_satuan'],
			harga_beli = request.POST['harga_beli'],			
			harga_jual = request.POST['harga_jual'],			
			stock = request.POST['stock'],			
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/obat/")
	context = {	
	'Tambah_suplier':'Tambah_suplier',
	'kode': kode,
	'select_satuan': select_satuan,
	'select_kategori': select_kategori,
	'select_suplier': select_suplier,
	}
	return render(request, 'Master_data/data_obat/tambah.html',  context)

def Hapus_obat(request, hapus_o):
	Model_obat.objects.filter(id=hapus_o).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('obat')

def Edit_obat(request, id_o):		
	edit_data = Model_obat.objects.get(id=id_o)
	if request.method == 'POST':		
			edit_data.kode_obat = request.POST.get('kode_obat')
			edit_data.nama_obat = request.POST.get('nama_obat')
			edit_data.nama_suplier = request.POST.get('nama_suplier')
			edit_data.nama_kategori = request.POST.get('nama_kategori')
			edit_data.nama_satuan = request.POST.get('nama_satuan')
			edit_data.harga_beli = request.POST.get('harga_beli')
			edit_data.harga_jual = request.POST.get('harga_jual')
			edit_data.stock = request.POST.get('stock')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('obat')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_obat/edit.html',  context)

# data kadalursa
def Data_kadaluarsa(request):	
	data = Model_kadaluarsa.objects.all()
	context = {
	'page_title':'Tabel',
	'data': data,
	}
	return render(request, 'Master_data/Data_kadaluarsa/tabel.html',  context)

def Tambah_kadaluarsa(request):
	kode_otomatis = Model_kadaluarsa.objects.count()
	
	select_data = Model_kategori.objects.all()
	select_suplier = Model_suplier.objects.all()

	if 'cari_data' in request.GET:
		cari_data=request.GET['cari_data']
		data_obat = Model_kategori.objects.filter(id=cari_data)
	else:
		data_obat = Model_kategori.objects.filter(id=None)	

	if request.method == 'POST':
		Model_kadaluarsa.objects.create(
			kode_kadar = request.POST['kode_kadar'],
			nama_obat = request.POST['nama_obat'],
			nama_suplier = request.POST['nama_suplier'],
			tanggal_kadar = request.POST['tanggal_kadar'],
			status = request.POST['status'],		
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/kadar/")
	context = {	
	'Tambah_suplier':'Tambah_suplier',
	'data_obat': data_obat,
	'select_data': select_data,
	'select_suplier': select_suplier,
	'kode_otomatis': kode_otomatis,
	}
	return render(request, 'Master_data/Data_kadaluarsa/tambah.html',  context)

def Hapus_kadaluarsa(request, hapus_k):
	Model_kadaluarsa.objects.filter(id=hapus_k).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('kadar')

def Edit_kadaluarsa(request, id_k):		
	edit_data = Model_kadaluarsa.objects.get(id=id_k)
	select_data = Model_kategori.objects.all()
	select_suplier = Model_suplier.objects.all()
	if request.method == 'POST':		
			edit_data.kode_kadar = request.POST.get('kode_kadar')
			edit_data.nama_obat = request.POST.get('nama_obat')
			edit_data.nama_suplier = request.POST.get('nama_suplier')
			edit_data.tanggal_kadar = request.POST.get('tanggal_kadar')
			edit_data.status = request.POST.get('status')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('kadar')

	context = {
	'edit_data': edit_data,
	'select_data': select_data,
	'select_suplier': select_suplier,
	}
	return render(request, 'Master_data/Data_kadaluarsa/edit.html',  context)

# data pembelian obat
def Data_pembelian(request):	
	data = Model_pembelian.objects.all()
	context = {
	'page_title':'Tabel',
	'data': data,
	}
	return render(request, 'Master_data/data_pembelian/tabel.html',  context)

def Proses_pembelian(request, id_pro):		
	proses = Model_suplier.objects.get(id=id_pro)
	kode = Model_pembelian.objects.count()
	kode_otomatis = kode + 1 ;

	if request.method == 'POST':
		Model_pembelian.objects.create(
			nota = request.POST['nota'],
			nama_pembelian = request.POST['nama_pembelian'],
			kode_suplier = request.POST['kode_suplier'],
			nama_suplier = request.POST['nama_suplier'],
			tgl_pembelian = request.POST['tgl_pembelian'],
			harga = request.POST['harga'],
			jumlah = request.POST['jumlah'],
			total = request.POST['total'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/pembelian/")		
	context = {
	'proses': proses,
	'kode_otomatis': kode_otomatis,
	}
	return render(request, 'Master_data/data_pembelian/proses.html',  context)

def Tambah_pembelian(request):
	kode = Model_pembelian.objects.count()
	kode_otomatis = kode + 1 ;

	data = Model_suplier.objects.all()
	if request.method == 'POST':
		Model_pembelian.objects.create(
			nota = request.POST['nota'],
			nama_pembelian = request.POST['nama_pembelian'],
			kode_suplier = request.POST['kode_suplier'],
			nama_suplier = request.POST['nama_suplier'],
			tgl_pembelian = request.POST['tgl_pembelian'],
			harga = request.POST['harga'],
			jumlah = request.POST['jumlah'],
			total = request.POST['total'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/pembelian/")		
	context = {	
	'Tambah_satuan':'Tambah_satuan',
	'kode_otomatis': kode_otomatis,
	'data': data,
	}
	return render(request, 'Master_data/data_pembelian/tambah.html',  context)

def Hapus_pembelian(request, hapus_pm):
	Model_pembelian.objects.filter(id=hapus_pm).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('pembelian')

def Edit_pembelian(request, id_pm):		
	edit_data = Model_pembelian.objects.get(id=id_pm)
	if request.method == 'POST':		
			edit_data.nota = request.POST.get('nota')
			edit_data.nama_pembelian = request.POST.get('nama_pembelian')
			edit_data.kode_suplier = request.POST.get('kode_suplier')
			edit_data.nama_suplier = request.POST.get('nama_suplier')
			edit_data.tgl_pembelian = request.POST.get('tgl_pembelian')
			edit_data.harga = request.POST.get('harga')
			edit_data.jumlah = request.POST.get('jumlah')
			edit_data.total = request.POST.get('total')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('pembelian')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_pembelian/edit.html',  context)	

# data penjualan
def Data_penjualan(request):	
	data = Model_penjualan1.objects.all()
	context = {
	'page_title':'Tabel',
	'data': data,
	}
	return render(request, 'Master_data/data_penjualan/tabel.html',  context)

def Proses_penjualan(request, id_prs):
	proses_data = Model_obat.objects.get(id=id_prs)
	kode = Model_penjualan1.objects.count()
	kode_otomatis = kode + 1 ;
	if request.method == 'POST':
		Model_penjualan1.objects.create(
			nota_penjualan = request.POST['nota_penjualan'],
			kode_obat = request.POST['kode_obat'],
			nama_obat = request.POST['nama_obat'],
			nama_kategori = request.POST['nama_kategori'],
			harga = request.POST['harga'],
			jumlah = request.POST['jumlah'],
			total = request.POST['total'],
			bayar = request.POST['bayar'],
			kembalian = request.POST['kembalian'],
			tanggal = request.POST['tanggal'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/penjualan/")		
	context = {
	'page_title':'Tabel',
	'proses_data': proses_data,
	'kode_otomatis': kode_otomatis,
	}
	return render(request, 'Master_data/data_penjualan/proses.html',  context)

def Tambah_penjualan(request):
	data = Model_obat.objects.all()

	kode = Model_penjualan1.objects.count()
	kode_otomatis = kode + 1 ;
	
	context = {	
	'Tambah_penjualan':'Tambah_penjualan',
	'kode_otomatis': kode_otomatis,
	'data': data,
	}
	return render(request, 'Master_data/data_penjualan/tambah.html',  context)

def Hapus_penjualan(request, hapus_pn):
	Model_penjualan1.objects.filter(id=hapus_pn).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('penjualan')

def Nota_penjualan(request, nota):
	nota_data = Model_penjualan1.objects.get(id=nota)
	context = {	
	'nota_data': nota_data,
	}
	return render(request, 'Master_data/data_penjualan/nota.html',  context)

def Edit_penjualan(request, id_pn):
	edit_data = Model_penjualan1.objects.get(id=id_pn)
	if request.method == 'POST':		
			edit_data.nota_penjualan = request.POST.get('nota_penjualan')
			edit_data.kode_obat = request.POST.get('kode_obat')
			edit_data.nama_obat = request.POST.get('nama_obat')
			edit_data.nama_kategori = request.POST.get('nama_kategori')
			edit_data.harga = request.POST.get('harga')
			edit_data.jumlah = request.POST.get('jumlah')
			edit_data.total = request.POST.get('total')
			edit_data.bayar = request.POST.get('bayar')
			edit_data.kembalian = request.POST.get('kembalian')
			edit_data.tanggal = request.POST.get('tanggal')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('penjualan')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_penjualan/edit.html',  context)

# menu laporan
def Menu_laporan(request):	
	context = {
	'page_title':'Tabel',
	}
	return render(request, 'Master_data/Laporan/menu.html',  context)

# lp obat
def lp_obat(request):	
	data = Model_obat.objects.all()
	context = {
	'page_title':'Tabel',
	'data': data,
	}
	return render(request, 'Master_data/Laporan/lp_obat.html',  context)

def lp_suplier(request):	
	data = Model_suplier.objects.all()
	context = {
	'page_title':'Tabel',
	'data': data,
	}
	return render(request, 'Master_data/Laporan/lp_suplier.html',  context)	

def lp_kadaluarsa(request):	
	data = Model_kadaluarsa.objects.all()
	context = {
	'page_title':'Tabel',
	'data': data,
	}
	return render(request, 'Master_data/Laporan/lp_kadaluarsa.html',  context)	

# *args, **kwargs,
def lp_pembelian(request, *args, **kwargs):	
	data = Model_pembelian.objects.all()
	sub_total = Model_pembelian.objects.aggregate(Total=Sum('total'))['Total']
	
	context = {
	'page_title':'Tabel',
	'data': data,
	'sub_total': sub_total
	}
	return render(request, 'Master_data/Laporan/lp_pembelian.html',  context)	

def lp_pembelian_tgl(request):	
	if 'cari_data' in request.GET:
		cari_data=request.GET['cari_data']
		data = Model_pembelian.objects.filter(tgl_pembelian=cari_data)
	else:
		data = Model_pembelian.objects.filter(tgl_pembelian=None)	

	sub_total = Model_pembelian.objects.aggregate(Total=Sum('total'))['Total']
	
	context = {
	'page_title':'Tabel',
	'data': data,
	'sub_total': sub_total
	}
	return render(request, 'Master_data/Laporan/lp_pembelian_tgl.html',  context)	

# lp penjualan
def lp_penjualan(request):	
	data = Model_penjualan1.objects.all()
	sub_total = Model_penjualan1.objects.aggregate(Total=Sum('total'))['Total']
	context = {
	'page_title':'Tabel',
	'data': data,
	'sub_total': sub_total,	
	}
	return render(request, 'Master_data/Laporan/lp_penjualan.html',  context)	

def lp_penjualan_tgl(request):	
	if 'cari_data' in request.GET:
		cari_data=request.GET['cari_data']
		data = Model_penjualan1.objects.filter(tanggal=cari_data)
	else:
		data = Model_penjualan1.objects.filter(tanggal=None)	

	sub_total = Model_penjualan1.objects.aggregate(Total=Sum('total'))['Total']
	context = {
	'page_title':'Tabel',
	'data': data,
	'sub_total': sub_total,	
	}
	return render(request, 'Master_data/Laporan/lp_penjualan_tgl.html',  context)		
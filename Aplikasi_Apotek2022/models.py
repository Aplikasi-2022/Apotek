from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.
class Model_kategori(models.Model):
	kode_kategori	= models.CharField(max_length = 12)
	nama_kategori	=models.CharField(max_length = 1200)
	harga	=models.CharField(max_length = 25)
	gambar	=models.ImageField(upload_to ='Berkas/', null=True)	
	keterangan	=models.CharField(max_length = 12000)	

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_kategori)

# data satuan
class Model_satuan(models.Model):
	kode_satuan	= models.CharField(max_length = 12)
	nama_satuan	=models.CharField(max_length = 1200)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_satuan)

# data suplier
class Model_suplier(models.Model):
	kode_suplier	= models.CharField(max_length = 12)
	nama_suplier	=models.CharField(max_length = 1200)
	lokasi	=models.CharField(max_length = 1200)
	telp	=models.CharField(max_length = 12)
	email	=models.CharField(max_length = 1200)
	alamat	=models.CharField(max_length = 1200)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_suplier)

# data obat
class Model_obat(models.Model):
	kode_obat	= models.CharField(max_length = 12)
	nama_obat	=models.CharField(max_length = 1200)
	nama_suplier	=models.CharField(max_length = 1200)
	nama_kategori	=models.CharField(max_length = 1200)
	nama_satuan	=models.CharField(max_length = 1200)
	harga_beli	=models.CharField(max_length = 12)
	harga_jual	=models.CharField(max_length = 12)
	stock	=models.CharField(max_length = 12)	

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_obat)

# data kada luarsa
class Model_kadaluarsa(models.Model):
	kode_kadar	= models.CharField(max_length = 12)
	nama_obat	=models.CharField(max_length = 1200)
	nama_suplier	=models.CharField(max_length = 1200)
	tanggal_kadar	=models.CharField(max_length = 1200)
	status	=models.CharField(max_length = 1200)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_obat)

# data pembelian
class Model_pembelian(models.Model):
	nota	= models.CharField(max_length = 12)
	nama_pembelian	=models.CharField(max_length = 1200)
	kode_suplier	=models.CharField(max_length = 1200)
	nama_suplier	=models.CharField(max_length = 1200)
	tgl_pembelian	=models.CharField(max_length = 1200)
	harga	=models.CharField(max_length = 1200)
	jumlah	=models.CharField(max_length = 12)
	total	=models.CharField(max_length = 12)	

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_pembelian)


# data penjualan
class Model_penjualan1(models.Model):
	nota_penjualan	= models.CharField(max_length = 12)
	kode_obat	=models.CharField(max_length = 1200)
	nama_obat	=models.CharField(max_length = 1200)
	nama_kategori	=models.CharField(max_length = 1200)
	harga	=models.CharField(max_length = 12)
	jumlah	=models.CharField(max_length = 12)
	total	=models.CharField(max_length = 12)
	bayar	=models.CharField(max_length = 12)
	kembalian	=models.CharField(max_length = 12)	
	tanggal	=models.CharField(max_length = 25)	

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_obat)
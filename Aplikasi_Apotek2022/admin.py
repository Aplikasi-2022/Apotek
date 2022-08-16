from django.contrib import admin

# Register your models here. daftar model yang telah kita buat
from .models import Model_kategori, Model_satuan, Model_suplier, Model_obat, Model_kadaluarsa, Model_pembelian, Model_penjualan1

admin.site.register(Model_kategori)
admin.site.register(Model_satuan)
admin.site.register(Model_suplier)
admin.site.register(Model_obat)
admin.site.register(Model_kadaluarsa)
admin.site.register(Model_pembelian)
admin.site.register(Model_penjualan1)
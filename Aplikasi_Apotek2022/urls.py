from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from Aplikasi_Apotek2022 import settings
from django.urls import path
# from django.contrib.auth import views
from django.contrib import admin
from . import views

from .views import index, HomeView, LogoutView, Data_kategori, Tambah_kategori, Edit_kategori, Hapus_kategori, Data_satuan, Tambah_satuan, Edit_satuan, Hapus_satuan, Data_suplier, Tambah_suplier, Edit_suplier, Hapus_suplier, Data_obat, Tambah_obat, Edit_obat, Hapus_obat, Data_kadaluarsa, Tambah_kadaluarsa, Edit_kadaluarsa, Hapus_kadaluarsa, Data_pembelian, Tambah_pembelian, Edit_pembelian, Hapus_pembelian, Proses_pembelian, Data_penjualan, Tambah_penjualan, Edit_penjualan, Hapus_penjualan, Proses_penjualan, Nota_penjualan, Menu_laporan, lp_obat, lp_suplier, lp_kadaluarsa, lp_pembelian, lp_penjualan, lp_pembelian_tgl, lp_penjualan_tgl
from django.contrib import admin
from django.urls import path
urlpatterns = [
    url(r'^$',index, name="index"),
    url(r'^Home/$', HomeView, name="Home"),
    url(r'^logout/$',LogoutView, name="logout"),
    # kategori
    url(r'^kategori/$', Data_kategori, name="kategori"),
    url(r'^tambah_kategori/$', Tambah_kategori, name="tambah_kategori"),
    url(r'^hapus_kategori/(?P<hapus_k>[0-9]+)$',Hapus_kategori, name="hapus_kategori"),
    url(r'^edit_kategori/(?P<id_k>[0-9]+)$',Edit_kategori, name="edit_kategori"),

    # data satuan
    url(r'^satuan/$', Data_satuan, name="satuan"),
    url(r'^tambah_satuan/$', Tambah_satuan, name="tambah_satuan"),
    url(r'^hapus_satuan/(?P<hapus_s>[0-9]+)$',Hapus_satuan, name="hapus_satuan"),
    url(r'^edit_satuan/(?P<id_s>[0-9]+)$',Edit_satuan, name="edit_satuan"),

    # data suplier
    url(r'^suplier/$', Data_suplier, name="suplier"),
    url(r'^tambah_suplier/$', Tambah_suplier, name="tambah_suplier"),
    url(r'^hapus_suplier/(?P<hapus_sp>[0-9]+)$',Hapus_suplier, name="hapus_suplier"),
    url(r'^edit_suplier/(?P<id_sp>[0-9]+)$',Edit_suplier, name="edit_suplier"),

    # data obat
    url(r'^obat/$', Data_obat, name="obat"),
    url(r'^tambah_obat/$', Tambah_obat, name="tambah_obat"),
    url(r'^hapus_obat/(?P<hapus_o>[0-9]+)$',Hapus_obat, name="hapus_obat"),
    url(r'^edit_obat/(?P<id_o>[0-9]+)$',Edit_obat, name="edit_obat"),

    # data kadaluarsa
    url(r'^kadar/$', Data_kadaluarsa, name="kadar"),
    url(r'^tambah_kadaluarsa/$', Tambah_kadaluarsa, name="tambah_kadaluarsa"),
    url(r'^hapus_kadaluarsa/(?P<hapus_k>[0-9]+)$',Hapus_kadaluarsa, name="hapus_kadaluarsa"),
    url(r'^edit_kadaluarsa/(?P<id_k>[0-9]+)$',Edit_kadaluarsa, name="edit_kadaluarsa"),

    # pembelian obat
    url(r'^pembelian/$', Data_pembelian, name="pembelian"),
    url(r'^tambah_pembelian/$', Tambah_pembelian, name="tambah_pembelian"),
    url(r'^proses_pembelian/(?P<id_pro>[0-9]+)$',Proses_pembelian, name="proses_pembelian"),
    url(r'^hapus_pembelian/(?P<hapus_pm>[0-9]+)$',Hapus_pembelian, name="hapus_pembelian"),
    url(r'^edit_pembelian/(?P<id_pm>[0-9]+)$',Edit_pembelian, name="edit_pembelian"),

    # data penjualan
    url(r'^penjualan/$', Data_penjualan, name="penjualan"),
    url(r'^tambah_penjualan/$', Tambah_penjualan, name="tambah_penjualan"),
    url(r'^proses_penjualan/(?P<id_prs>[0-9]+)$',Proses_penjualan, name="proses_penjualan"),
    url(r'^nota_penjualan/(?P<nota>[0-9]+)$',Nota_penjualan, name="nota_penjualan"),    
    url(r'^hapus_penjualan/(?P<hapus_k>[0-9]+)$',Hapus_penjualan, name="hapus_penjualan"),
    url(r'^edit_penjualan/(?P<id_k>[0-9]+)$',Edit_penjualan, name="edit_penjualan"),


    # menu laporan
    url(r'^menu_laporan/$', Menu_laporan, name="menu_laporan"),
    # laporan
    url(r'^lp_obat/$', lp_obat, name="lp_obat"),
    url(r'^lp_suplier/$', lp_suplier, name="lp_suplier"),
    url(r'^lp_kadaluarsa/$', lp_kadaluarsa, name="lp_kadaluarsa"),
    url(r'^lp_pembelian/$', lp_pembelian, name="lp_pembelian"),
    url(r'^lp_pembelian_tgl/$', lp_pembelian_tgl, name="lp_pembelian_tgl"),

    url(r'^lp_penjualan/$', lp_penjualan, name="lp_penjualan"),
    url(r'^lp_penjualan_tgl/$', lp_penjualan_tgl, name="lp_penjualan_tgl"),


    path('admin/', admin.site.urls),
]

if settings.DEBUG:    
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
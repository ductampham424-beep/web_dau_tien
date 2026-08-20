from django.contrib import admin
from .models import DanhMuc, SanPham, TinTuc, LienHe

@admin.register(DanhMuc)
class DanhMucAdmin(admin.ModelAdmin):
    list_display = ('id', 'ten_danh_muc', 'slug')
    prepopulated_fields = {'slug': ('ten_danh_muc',)} # Tự động tạo slug khi gõ tên danh mục

@admin.register(SanPham)
class SanPhamAdmin(admin.ModelAdmin):
    list_display = ('id', 'ten_san_pham', 'danh_muc', 'gia', 'ngay_tao')
    list_filter = ('danh_muc',)
    search_fields = ('ten_san_pham',)

@admin.register(TinTuc)
class TinTucAdmin(admin.ModelAdmin):
    list_display = ('id', 'tieu_de', 'ngay_dang')

@admin.register(LienHe)
class LienHeAdmin(admin.ModelAdmin):
    list_display = ('id', 'ho_ten', 'so_dien_thoai', 'ngay_gui')
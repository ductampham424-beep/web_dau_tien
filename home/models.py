from django.db import models

# --- THÊM MỚI 1: Bảng Danh mục (để làm các tab: Xây lắp nhà xưởng, Kết cấu thép...) ---
class DanhMuc(models.Model):
    ten_danh_muc = models.CharField(max_length=200, verbose_name="Tên danh mục")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Đường dẫn SEO")

    class Meta:
        verbose_name_plural = "1. Danh mục dịch vụ"

    def __str__(self):
        return self.ten_danh_muc


# --- BẢNG CỦA BẠN (Đã thêm nối với DanhMuc) ---
class SanPham(models.Model):
    # Thêm trường này để biết Sản phẩm/Dự án thuộc danh mục nào
    danh_muc = models.ForeignKey(DanhMuc, on_delete=models.CASCADE, related_name='san_pham', null=True, blank=True, verbose_name="Danh mục")
    
    ten_san_pham = models.CharField(max_length=200) # Tên sản phẩm
    gia = models.CharField(max_length=100, default="Liên hệ") # Giá sản phẩm
    mo_ta = models.TextField(blank=True) # Mô tả chi tiết
    anh_san_pham = models.ImageField(upload_to='san_pham/', blank=True, null=True) # Ô đăng ảnh
    ngay_tao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "2. Sản phẩm & Dự án"

    def __str__(self):
        return self.ten_san_pham


# --- BẢNG CỦA BẠN (Đã thêm ảnh đại diện bài viết) ---
class TinTuc(models.Model):
    tieu_de = models.CharField(max_length=255) # Tiêu đề bài viết
    tom_tat = models.TextField(blank=True)      # Giới thiệu ngắn
    noi_dung = models.TextField(blank=True, null=True) # Nội dung chi tiết bài viết
    anh_dai_dien = models.ImageField(upload_to='tin_tuc/', blank=True, null=True) # Ảnh bài viết
    ngay_dang = models.DateTimeField(auto_now_add=True) # Tự động lấy ngày đăng

    class Meta:
        verbose_name_plural = "3. Tin tức & Sự kiện"

    def __str__(self):
        return self.tieu_de


# --- THÊM MỚI 2: Bảng Lưu thông tin khi khách hàng gửi Form "Liên hệ" ---
class LienHe(models.Model):
    ho_ten = models.CharField(max_length=100, verbose_name="Họ và tên")
    so_dien_thoai = models.CharField(max_length=20, verbose_name="Số điện thoại")
    email = models.EmailField(blank=True, verbose_name="Email")
    noi_dung = models.TextField(verbose_name="Nội dung cần tư vấn")
    ngay_gui = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "4. Khách hàng liên hệ"

    def __str__(self):
        return f"{self.ho_ten} - {self.so_dien_thoai}"
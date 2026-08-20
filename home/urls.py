from django.urls import path
from . import views

urlpatterns = [
    path('', views.trang_chu, name='trang_chu'),
    
    # TRANG DANH SÁCH SẢN PHẨM:
    path('san-pham/', views.danh_sach_san_pham, name='san_pham'),
    
    # TRANG CHI TIẾT SẢN PHẨM:
    path('san-pham/<int:sp_id>/', views.chi_tiet_san_pham, name='chi_tiet_san_pham'),
    
    # TRANG TIN TỨC:
    path('tin-tuc/', views.trang_tin_tuc, name='tin_tuc'),
    
    # GIỚI THIỆU:
    path('gioi-thieu/', views.gioi_thieu, name='gioi_thieu'),
    
    # XỬ LÝ GỬI FORM LIÊN HỆ (ĐÃ THÊM MỚI):
    path('gui-lien-he/', views.gui_lien_he, name='gui_lien_he'),
]
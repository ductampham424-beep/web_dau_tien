from django.shortcuts import render, get_object_or_404, redirect
from .models import DanhMuc, SanPham, TinTuc, LienHe

def trang_chu(request):
    q = request.GET.get('q', '')
    if q:
        ds_san_pham = SanPham.objects.filter(ten_san_pham__icontains=q)
    else:
        ds_san_pham = SanPham.objects.all()
    
    ds_danh_muc = DanhMuc.objects.all()
    ds_tin_tuc = TinTuc.objects.all().order_by('-ngay_dang')[:3]
    
    context = {
        'ds_san_pham': ds_san_pham,
        'ds_danh_muc': ds_danh_muc,
        'ds_tin_tuc': ds_tin_tuc,
        'q': q,
    }
    return render(request, 'home/index.html', context)

def chi_tiet_san_pham(request, sp_id):
    san_pham = get_object_or_404(SanPham, id=sp_id)
    return render(request, 'home/chi_tiet.html', {'san_pham': san_pham})

def trang_tin_tuc(request):
    ds_tin_tuc = TinTuc.objects.all()
    return render(request, 'home/tin_tuc.html', {'ds_tin_tuc': ds_tin_tuc})

def danh_sach_san_pham(request):
    danh_muc_id = request.GET.get('danh_muc')
    q = request.GET.get('q', '')
    
    ds_san_pham = SanPham.objects.all()
    if danh_muc_id:
        ds_san_pham = ds_san_pham.filter(danh_muc_id=danh_muc_id)
    if q:
        ds_san_pham = ds_san_pham.filter(ten_san_pham__icontains=q)
        
    ds_danh_muc = DanhMuc.objects.all()
    return render(request, 'home/san_pham.html', {
        'ds_san_pham': ds_san_pham,
        'ds_danh_muc': ds_danh_muc,
        'q': q
    })

def gioi_thieu(request):
    return render(request, 'home/gioi_thieu.html')

def gui_lien_he(request):
    if request.method == 'POST':
        ho_ten = request.POST.get('ho_ten')
        so_dien_thoai = request.POST.get('so_dien_thoai')
        email = request.POST.get('email', '')
        noi_dung = request.POST.get('noi_dung', '')
        
        LienHe.objects.create(
            ho_ten=ho_ten,
            so_dien_thoai=so_dien_thoai,
            email=email,
            noi_dung=noi_dung
        )
    return redirect('trang_chu')

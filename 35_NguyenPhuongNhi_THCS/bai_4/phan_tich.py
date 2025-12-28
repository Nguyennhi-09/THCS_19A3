from du_lieu import danh_sach,tu_dien
so = [11,9,10,19,7,14,29,22]
gia_tri = {
    "ten":"Nguyễn Phương Nhi",
    "tuoi":18,
    "gioi_tinh":"Nữ"
}

print("sắp xếp tăng dần: ",danh_sach.sap_xep_tang_dan(so))
print("lấy giá trị",tu_dien.lay_gia_tri(gia_tri,"ten"))
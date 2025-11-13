gia_san_pham = float(input("Nhập giá sản phẩm: "))
so_luong = int(input("Nhập số lượng mua: "))

tong_chi_phi = gia_san_pham * so_luong

vat = tong_chi_phi * 0.10

tong_tien = tong_chi_phi + vat

print("Tổng tiền phải trả (đã gồm VAT):{:.2f}".format(tong_tien))
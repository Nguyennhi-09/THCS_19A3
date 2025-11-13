ten_dang_nhap = input("Nhập tên đăng nhập: ")
mat_khau = input("Nhập mật khẩu: ")

truy_cap = (ten_dang_nhap == "admin") and (mat_khau != "password123")

print("Truy cập thành công:", truy_cap)


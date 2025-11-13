luong_co_ban = float(input("Nhập mức lương cơ bản (VNĐ): "))
ngay_cong = int(input("Nhập số ngày công trong tháng: "))

luong_ngay = luong_co_ban / 22

luong_thang = luong_ngay * ngay_cong

thuong = luong_thang * 0.10 * (ngay_cong > 22)
phat = luong_thang * 0.05 * (ngay_cong < 22)

tong_luong = luong_thang + thuong - phat

print(f"Tổng lương thực nhận là: {tong_luong:.2f} VNĐ")


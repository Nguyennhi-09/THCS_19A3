tien_goc = float(input("Nhập số tiền gửi ban đầu (VNĐ): "))
lai_suat_nam = float(input("Nhập lãi suất hàng năm (%): "))

lai_suat = lai_suat_nam / 100

lai_1_thang = tien_goc * lai_suat * (1/12)
lai_2_quy = tien_goc * lai_suat * (6/12)
lai_3_nam = tien_goc * lai_suat * 3

print(f"Lãi sau 1 tháng: {lai_1_thang:.2f} VNĐ")
print(f"Lãi sau 2 quý (6 tháng): {lai_2_quy:.2f} VNĐ")
print(f"Lãi sau 3 năm: {lai_3_nam:.2f} VNĐ")


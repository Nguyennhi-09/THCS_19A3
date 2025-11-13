so_kwh = int(input("Nhập số kWh điện đã tiêu thụ: "))

gia_bac_1 = 1678
gia_bac_2 = 1734
gia_bac_3 = 2014

bac_1 = min(so_kwh, 100)
bac_2 = min(max(so_kwh - 100, 0), 100)
bac_3 = min(max(so_kwh - 200, 0), 100)

tong_tien = bac_1 * gia_bac_1 + bac_2 * gia_bac_2 + bac_3 * gia_bac_3
print("Tổng tiền điện phải trả là:", tong_tien, "VNĐ")


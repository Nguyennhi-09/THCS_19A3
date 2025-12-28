with open("san_pham.txt", "w", encoding="utf-8") as f:
    f.write("ID, Tên sản phẩm, Giá\n")
    f.write("1, Laptop, 1200\n")
    f.write("2, Chuột máy tính, 25\n")
    f.write("3, Bàn phím, 75\n")

id_can_sua = input("Nhập ID sản phẩm cần cập nhật: ")
gia_moi = input("Nhập giá mới: ")

with open("san_pham.txt", "r", encoding="utf-8") as f:
    cac_dong = f.readlines()

danh_sach_moi = []

for dong in cac_dong:
    dong = dong.strip()

    if dong == "ID, Tên sản phẩm, Giá":
        danh_sach_moi.append(dong + "\n")
        continue

    phan = dong.split(", ")

    if phan[0] == id_can_sua:
        dong_moi = phan[0] + ", " + phan[1] + ", " + gia_moi + "\n"
        danh_sach_moi.append(dong_moi)
    else:
        danh_sach_moi.append(dong + "\n")

with open("san_pham.txt", "w", encoding="utf-8") as f:
    for dong in danh_sach_moi:
        f.write(dong)

print("Đã cập nhật giá sản phẩm thành công.")
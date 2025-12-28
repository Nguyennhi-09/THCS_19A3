with open("vanban.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()

# ........Tách từ
danh_sach_tu = noi_dung.split()

#  Tạo từ điển lưu tần suất
tan_suat = {}

for tu in danh_sach_tu:
    tu = tu.lower().strip(",.")  # viết thường hết
    if tu in tan_suat:
        tan_suat[tu] += 1 # nếu có rồi thì từ đấy + 1
    else:
        tan_suat[tu] = 1

print("Tần suất xuất hiện của các từ:")
for tu, so_lan in tan_suat.items():
    print(f"Từ '{tu}' xuất hiện {so_lan} lần")
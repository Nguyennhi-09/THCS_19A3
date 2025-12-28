ds_so_nguyen = [9, 10, 11, 24, 25]

with open("so_nguyen.txt", "w", encoding="utf-8") as f:
    for so in ds_so_nguyen:
        f.write(str(so) + "\n") 

print("Đã ghi danh sách số nguyên vào file so_nguyen.txt")

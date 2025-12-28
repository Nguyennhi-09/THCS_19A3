file_nguon = "file_nguon.bin"
file_dich = "file_dich.bin"

with open(file_nguon, "wb") as f:
    f.write(b"Day la noi dung cua file nguon.")

with open(file_nguon, "rb") as f_nguon:
    with open(file_dich, "wb") as f_dich:
        while True:
            du_lieu = f_nguon.read(1024)
            if not du_lieu:
                break
            f_dich.write(du_lieu)

print("Sao chép tập tin thành công.")

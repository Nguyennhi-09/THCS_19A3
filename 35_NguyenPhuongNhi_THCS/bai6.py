nam = int(input("Nhập một năm: "))

nam_nhuan = (nam % 400 == 0) or ((nam % 4 == 0) and (nam % 100 != 0))

print(nam, "là năm nhuận:", nam_nhuan)

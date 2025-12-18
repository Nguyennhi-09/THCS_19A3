chuoi = input("Nhập vào một chuỗi:")
chu = 0 
so = 0
ky_tu_dac_biet = 0

for i in chuoi:
    if('a' <= i <= 'z') or ('A' <= i <= 'Z'):
      chu += 1
    elif '0' <= i <= '9':
       so += 1
    else:
       ky_tu_dac_biet += 1
print("Chữ cái:", chu)
print("Chữ số:", so)
print("Ký tự đặc biệt:", ky_tu_dac_biet)
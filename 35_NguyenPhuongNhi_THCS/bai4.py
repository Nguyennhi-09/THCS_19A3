n = int(input("Nhập vào một số n: "))
print(f"các số nguyên tố nhỏ hơn {n} là: ")

for i in range(2,n):
    SoNguyenTo = True
    for j in range(2,i):
        if i % j == 0:
            SoNguyenTo = False
            break
        if SoNguyenTo:
            print(i,end="")
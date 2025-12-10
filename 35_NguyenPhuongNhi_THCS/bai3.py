n = int(input("Nhập vào một số nguyên dương n:"))
def kiem_tra_so_armstrong(n):
    tong = 0
    temp = n
    while temp > 0:
        chu_so = temp % 10
        tong += chu_so ** 3
        temp //= 10
    return tong == n
print(kiem_tra_so_armstrong(n))
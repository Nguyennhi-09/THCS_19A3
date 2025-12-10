def so_nguyen_to (n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0 :
            return False
    return True

print("các số nguyên tố từ 100 đến 500")
for i in range(100,500):
    if so_nguyen_to(i):
        print(i)

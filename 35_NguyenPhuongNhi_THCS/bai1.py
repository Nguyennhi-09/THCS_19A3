n = int(input("Nhập vào một số: "))
i = 0
while i <= n:
    if i*i == n:
        print(f"số{n}là số chính phương")
        break
    i += 1
else:
    print(f"số{n} không phải số chính phương")
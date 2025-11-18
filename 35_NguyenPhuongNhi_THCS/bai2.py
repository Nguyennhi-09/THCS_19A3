a = int(input("Nhập vào số a: "))
b = int(input("Nhập vào số b: "))
while a != b:
    if a>b:
        a=a-b
    else:
        b=b-a
print(f"ước chung lớn nhất của{a}và{b}là:",a)

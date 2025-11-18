a = int(input("nhập tử số: "))
b = int(input("nhập mẫu số(khác 0): "))

while b == 0:
    b = int(input("phương trình vô no, nhập lại: "))


dau = 1
if a * b < 0:
    dau = -1

a = abs(a)
b = abs(b)

i = 1
ucln = 1
while i <= a and i <= b:
    if a % i == 0 and b % i == 0:
        ucln = i
    i+=1


tu = (a // ucln) * dau
mau = b // ucln

print(f"Phân số tối giản của {a}/{b} là :",tu,"/",mau)
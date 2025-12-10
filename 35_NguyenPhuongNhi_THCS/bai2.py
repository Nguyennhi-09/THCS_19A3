a = int(input("NHập vào số a:"))
b = int (input("Nhập vào số b:"))
def giai_phuong_trinh_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        x = -b / a
        print("Nghiệm của phương trình là:", x)
print(giai_phuong_trinh_bac_nhat(a,b))
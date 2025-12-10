do_c = int(input("Nhập vào nhiệt độ C:"))
def chuyen_doi_nhiet_do(do_c):
    do_f = do_c * 9/5 + 32
    return do_f
print(chuyen_doi_nhiet_do(do_c))
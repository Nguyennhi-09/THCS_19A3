def kiem_tra_so_doi_xung(n):
    so_dao = 0
    so = n
    while n > 0:
        lay_so_cuoi = so % 10
        so_dao = so_dao * 10 + lay_so_cuoi
        so //= 10
        return so_dao == n

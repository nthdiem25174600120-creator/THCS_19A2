def kiem_tra_so_armstrong(n):
    so_ban_dau = n
    tong_luy_thua = 0
    if n < 0:
        return False
    while n > 0:
        chu_so = n % 10
        tong_luy_thua += chu_so ** 3
        n = n // 10
    if tong_luy_thua == so_ban_dau:
     return True
    else:
        return False

x = int(input("nhập số: "))
ket_qua = kiem_tra_so_armstrong(x)
print(ket_qua)
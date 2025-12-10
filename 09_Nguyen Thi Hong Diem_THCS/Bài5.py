def kiem_tra_so_doi_xung(n):
    so_ban_dau=n
    so_dao_nguoc=0
    if n<0:
        return False
    while n>0:
        chu_so=n%10
        so_dao_nguoc=so_dao_nguoc*10+chu_so
        n=n//10
    if so_dao_nguoc==so_ban_dau:
        return True
    else:
        return False
x=int(input("nhập 1 số: "))
kq=kiem_tra_so_doi_xung(x)
print(kq)
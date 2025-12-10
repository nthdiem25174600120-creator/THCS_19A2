def la_so_hoan_hao(n):
    if n <= 1:
        return False
    tong_uoc=0
    for i in range(1, n//2 +1):
        if n%i == 0:
            tong_uoc += i
    return tong_uoc == n


def tinh_tong_so_hoan_hao(a, b):
    tong_ket_qua=0
    if a > b:
        print("sai yêu cầu")
        return
    for i in range(a, b+1):
        if la_so_hoan_hao(i):
            tong_ket_qua += i
    return tong_ket_qua
x=int(input("nhập số a: "))
y=int(input("nhập số b: "))
kqua=tinh_tong_so_hoan_hao(x, y)
print(f"Tổng các số hoàn hảo trong khoảng từ {x} đến {y} là: ",kqua)
def la_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n%i==0:
            return False
    return True
v=int(input("nhập số nguyên: "))
kqua=la_so_nguyen_to(v)
print(kqua)

def in_so_nguyen_to_trong_khoang(a, b):
    if a>b:
        print("yêu cầu a < b ")
        return
    print(f"Các số nguyên tố trong khoảng từ {a} đến {b} là: ", end="")
    for x in range(a, b+1):
        if la_so_nguyen_to(x):
            print(x, end=" ")
s1_nguyen=int(input("nhập số a: "))
s2_nguyen=int(input("nhập số b: "))
in_so_nguyen_to_trong_khoang(s1_nguyen, s2_nguyen)
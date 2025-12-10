def tong_chu_so(n):
    if n < 0:
        n=abs(n)
    tong_chu_so=0
    while n > 0:
        chu_so=n%10
        tong_chu_so+=chu_so
        n=n//10
    return tong_chu_so
n_input = int(input("Nhập số nguyên dương n: "))
kq=tong_chu_so(n_input)
print(f"\nTổng các chữ số của {n_input} là:  ",kq)
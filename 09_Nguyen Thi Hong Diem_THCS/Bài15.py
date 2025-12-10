def so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
v=int(input("nhập số nguyên: "))
kqua=so_nguyen_to(v)
print(kqua)
for n in range(100, 501):
    if so_nguyen_to(n):
        print(n)
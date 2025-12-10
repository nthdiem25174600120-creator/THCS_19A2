def tim_so_le_lon_nhat(a, b, c):
    cac_so_le = []

    if a % 2 != 0:
        cac_so_le.append(a)

    if b % 2 != 0:
        cac_so_le.append(b)

    if c % 2 != 0:
        cac_so_le.append(c)

    if not cac_so_le:
        return -1
    else:
        return max(cac_so_le)

x=int(input("nhập số a: "))
y=int(input("nhập số b: "))
z=int(input("nhập số c: "))
kq=tim_so_le_lon_nhat(x, y, z)
print(f"số lẻ lớn nhất là: ",kq)
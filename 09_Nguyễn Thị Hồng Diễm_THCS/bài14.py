def tach_chuoi(chuoi):
    ds = []
    so_hien_tai = ""
    for ky_tu in chuoi:
        if ky_tu != " ":
            so_hien_tai += ky_tu
        else:
            if so_hien_tai != "":
                ds.append(int(so_hien_tai))
                so_hien_tai = ""
    if so_hien_tai != "":
        ds.append(int(so_hien_tai))
    return ds

chuoi_A = input("Nhập tập hợp A (các số cách nhau bởi khoảng trắng): ")
chuoi_B = input("Nhập tập hợp B (các số cách nhau bởi khoảng trắng): ")

A = tach_chuoi(chuoi_A)
B = tach_chuoi(chuoi_B)

hieu_A_B = []
for x in A:
    co_trong_B = False
    for y in B:
        if x == y:
            co_trong_B = True
            break
    if not co_trong_B and x not in hieu_A_B:
        hieu_A_B.append(x)

hieu_B_A = []
for x in B:
    co_trong_A = False
    for y in A:
        if x == y:
            co_trong_A = True
            break
    if not co_trong_A and x not in hieu_B_A:
        hieu_B_A.append(x)

giao = []
for x in A:
    for y in B:
        if x == y and x not in giao:
            giao.append(x)

hop = []
for x in A:
    if x not in hop:
        hop.append(x)
for y in B:
    if y not in hop:
        hop.append(y)

print("Các phần tử thuộc A nhưng không thuộc B:", hieu_A_B)
print("Các phần tử thuộc B nhưng không thuộc A:", hieu_B_A)
print("Các phần tử có trong cả A và B (giao):", giao)
print("Hợp của A và B:", hop)
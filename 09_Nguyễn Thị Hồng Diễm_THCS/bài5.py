chuoi = input("Nhập danh sách số nguyên, cách nhau bởi khoảng trắng: ")
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

ket_qua = []
for x in ds:
    da_co = False
    for y in ket_qua:
        if x == y:
            da_co = True
            break
    if not da_co:
        ket_qua.append(x)

print("Danh sách sau khi loại bỏ trùng lặp:")
for x in ket_qua:
    print(x, end=" ")
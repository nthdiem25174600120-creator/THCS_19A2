def tach_chuoi(chuoi):
    ds = []
    tam = ""
    for ky_tu in chuoi:
        if ky_tu != " ":
            tam += ky_tu
        else:
            if tam != "":
                ds.append(tam)
                tam = ""
    if tam != "":
        ds.append(tam)
    return ds

chuoi = input("Nhập các cặp key-value (key là chuỗi, value là số), cách nhau bởi khoảng trắng: ")

ds = tach_chuoi(chuoi)

d = {}
for i in range(0, len(ds), 2):
    key = ds[i]
    value = int(ds[i+1])
    d[key] = value

ket_qua = {}
for k in d:
    if d[k] > 50:   
        ket_qua[k] = d[k]

print("Dictionary gốc:", d)
print("Dictionary sau khi lọc (value > 50):", ket_qua)
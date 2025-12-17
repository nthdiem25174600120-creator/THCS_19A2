chuoi = input("Nhập các cặp tên-điểm (cách nhau bởi khoảng trắng): ")
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

d = {}
for i in range(0, len(ds), 2):
    ten = ds[i]
    diem = int(ds[i+1])
    d[ten] = diem

nhom = {}
for ten in d:
    diem = d[ten]
    if diem not in nhom:
        nhom[diem] = [ten]   
    else:
        nhom[diem].append(ten)  

print("Dictionary ban đầu:", d)
print("Dictionary sau khi nhóm theo điểm:", nhom)
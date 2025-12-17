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

k = int(input("Nhập số k (số vị trí dịch chuyển): "))

n = len(ds)
ket_qua = [0] * n   

for i in range(n):
    new_index = (i + k) % n
    ket_qua[new_index] = ds[i]

print("Danh sách sau khi dịch chuyển sang phải", k, "vị trí:")
for x in ket_qua:
    print(x, end=" ")
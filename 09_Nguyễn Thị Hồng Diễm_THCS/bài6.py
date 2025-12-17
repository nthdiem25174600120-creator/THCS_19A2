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

tong_chan = 0
tong_le = 0

for x in ds:
    if x % 2 == 0:
        tong_chan += x
    else:
        tong_le += x

print("Tổng các số chẵn:", tong_chan)
print("Tổng các số lẻ:", tong_le)
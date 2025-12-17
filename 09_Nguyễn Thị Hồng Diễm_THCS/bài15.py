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

chuoi = input("Nhập các số nguyên, cách nhau bởi khoảng trắng: ")
ds = tach_chuoi(chuoi)
tuple_goc = tuple(ds)

chan_list = []
le_list = []

for x in tuple_goc:
    if x % 2 == 0:
        chan_list.append(x)
    else:
        le_list.append(x)

tuple_chan = tuple(chan_list)
tuple_le = tuple(le_list)

tong_chan = 0
for x in tuple_chan:
    tong_chan += x

tong_le = 0
for x in tuple_le:
    tong_le += x

print("Tuple ban đầu:", tuple_goc)
print("Tuple chứa số chẵn:", tuple_chan)
print("Tuple chứa số lẻ:", tuple_le)
print("Tổng các số chẵn:", tong_chan)
print("Tổng các số lẻ:", tong_le)
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

if len(ds) < 2:
    print("Danh sách phải có ít nhất 2 số nguyên.")
else:
    lon_nhat = ds[0]
    for x in ds:
        if x > lon_nhat:
            lon_nhat = x

    lon_thu_hai = None
    for x in ds:
        if x != lon_nhat:  
            if lon_thu_hai is None or x > lon_thu_hai:
                lon_thu_hai = x

    if lon_thu_hai is None:
        print("Không có giá trị lớn thứ hai (tất cả phần tử bằng nhau).")
    else:
        print("Giá trị lớn thứ hai là:", lon_thu_hai)
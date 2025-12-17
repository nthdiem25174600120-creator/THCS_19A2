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
target = int(input("Nhập giá trị tổng cần tìm: "))
print("Các cặp số có tổng bằng", target, ":")
for i in range(len(ds)):
    for j in range(i + 1, len(ds)):
        if ds[i] + ds[j] == target:
            print(ds[i], "+", ds[j], "=", target)
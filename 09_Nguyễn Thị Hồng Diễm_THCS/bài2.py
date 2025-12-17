chuoi = input("Nhập vào một chuỗi: ")
n = int(input("Nhập vào số n: "))
ds_tu = []
tu_hien_tai = ""

for ky_tu in chuoi:
    if ky_tu != " ":   
        tu_hien_tai += ky_tu
    else:
        if tu_hien_tai != "":
            ds_tu.append(tu_hien_tai)
            tu_hien_tai = ""

if tu_hien_tai != "":
    ds_tu.append(tu_hien_tai)

print("Các từ có độ dài lớn hơn", n, ":")
for tu in ds_tu:
    dem = 0
    for _ in tu:   
        dem += 1
    if dem > n:
        print(tu)
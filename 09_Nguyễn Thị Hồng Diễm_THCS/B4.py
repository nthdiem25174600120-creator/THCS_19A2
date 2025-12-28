with open("san_pham.txt", "w", encoding="utf-8") as f:
    f.write("ID, Tên sản phẩm, Giá\n")
    f.write("1, Laptop, 1200\n")
    f.write("2, Chuột máy tính, 25\n")
    f.write("3, Bàn phím, 75")
id = input("Nhập ID sản phẩm cần tìm: ")
gia_moi=input("Nhập giá mới:")
gia_update=[]
san_pham = False
with open("san_pham.txt", "r", encoding="utf-8") as f:
    noi_dung=f.readlines()
    gia_update.append(noi_dung[0])
    for line in noi_dung[1:]:
        ds=line.strip().split(", ")
        if ds[0]==id:
            ds[2]=gia_moi
            san_pham=True
        gia_update.append(", ".join(ds)+"\n")
if san_pham:
    with open("san_pham.txt", "w", encoding="utf-8") as f:
        f.writelines(gia_update)
    print("Cập nhật giá sản phẩm thành công.")
else:
    print("Không tìm thấy sản phẩm với ID đã nhập.")
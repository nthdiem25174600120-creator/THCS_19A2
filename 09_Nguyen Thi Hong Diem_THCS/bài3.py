tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
min_so = min(abs(tu), abs(mau))  
ucln = min_so
while ucln > 0:
    if tu % ucln == 0 and mau % ucln == 0:
        break 
    ucln -= 1  
tu_so_gian = tu // ucln
mau_so_gian = mau // ucln
print("Phân số tối giản là:", tu_so_gian, "/", mau_so_gian)
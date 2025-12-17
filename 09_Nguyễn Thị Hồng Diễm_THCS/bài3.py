chuoi = input("Nhập vào một chuỗi: ")
ket_qua = ""
trang_thai_trang = False   

for ky_tu in chuoi:
    if ky_tu == " ":
        
        if not trang_thai_trang and ket_qua != "":
            ket_qua += " "
        trang_thai_trang = True
    else:
        ket_qua += ky_tu
        trang_thai_trang = False

if len(ket_qua) > 0 and ket_qua[-1] == " ":
    ket_qua = ket_qua[:-1]

print("Chuỗi sau khi xóa khoảng trắng thừa:")
print(ket_qua)
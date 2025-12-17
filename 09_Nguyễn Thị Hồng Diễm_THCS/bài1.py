chuoi = input("Nhập vào một chuỗi: ")
so_chu_cai = 0
so_chu_so = 0
so_ky_tu_dac_biet = 0
for ky_tu in chuoi:
    ma_ascii = ord(ky_tu)
    if (65 <= ma_ascii <= 90) or (97 <= ma_ascii <= 122):
        so_chu_cai += 1
    elif 48 <= ma_ascii <= 57:
        so_chu_so += 1
    else:
        so_ky_tu_dac_biet += 1
print("Số lượng chữ cái:", so_chu_cai)
print("Số lượng chữ số:", so_chu_so)
print("Số lượng ký tự đặc biệt:", so_ky_tu_dac_biet)
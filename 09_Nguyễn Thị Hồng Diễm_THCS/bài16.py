chuoi = input("Nhập vào một chuỗi: ")
tan_suat = {}
for ky_tu in chuoi:
    if ky_tu in tan_suat:
        tan_suat[ky_tu] += 1   
    else:
        tan_suat[ky_tu] = 1    

print("Tần suất xuất hiện của mỗi ký tự:")
for ky_tu in tan_suat:
    print(f"'{ky_tu}': {tan_suat[ky_tu]}")
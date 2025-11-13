# Nhập số tiền gửi ban đầu và lãi suất hàng năm
tien_goc = float(input("Nhập số tiền gửi ban đầu (VNĐ): "))
lai_suat_nam = float(input("Nhập lãi suất hàng năm (%): "))
# Chuyển lãi suất sang dạng thập phân
lai_suat = lai_suat_nam / 100
# Tính lãi sau 1 tháng (1/12 năm)
lai_1_thang = tien_goc * lai_suat * (1/12)
# Tính lãi sau 2 quý (0.5 năm)
lai_2_quy = tien_goc * lai_suat * 0.5
# Tính lãi sau 3 năm
lai_3_nam = tien_goc * lai_suat * 3
# In kết quả
print(f"Lãi sau 1 tháng: {round(lai_1_thang, 2)} VNĐ")
print(f"Lãi sau 2 quý: {round(lai_2_quy, 2)} VNĐ")
print(f"Lãi sau 3 năm: {round(lai_3_nam, 2)} VNĐ")
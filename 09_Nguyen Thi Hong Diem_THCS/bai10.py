# Nhập lương cơ bản và số ngày công
luong_cb = float(input("Nhập mức lương cơ bản (VNĐ): "))
so_ngay_cong = float(input("Nhập số ngày công trong tháng: "))

# Tính lương một ngày
luong_1_ngay = luong_cb / 22

# Lương theo số ngày công
luong_thuc = luong_1_ngay * so_ngay_cong

# Tính tiền thưởng: 10% lương cơ bản nếu ngày công > 22
thuong = (so_ngay_cong > 22) * 0.10 * luong_cb

# Tính tiền phạt: 5% lương cơ bản nếu ngày công < 22
phat = (so_ngay_cong < 22) * 0.05 * luong_cb

# Tổng lương thực nhận
tong_luong = luong_thuc + thuong - phat

# In kết quả
print(f"Tổng lương thực nhận: {tong_luong} VNĐ")

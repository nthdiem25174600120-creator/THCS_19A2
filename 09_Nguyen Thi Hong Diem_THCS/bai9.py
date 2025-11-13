# Nhập số kWh điện đã tiêu thụ
so_kwh = float(input("Nhập số kWh điện đã tiêu thụ: "))

# Giá điện từng bậc
gia_bac1 = 1678
gia_bac2 = 1734
gia_bac3 = 2014

# Tính số kWh từng bậc
# Bậc 1: tối đa 100 kWh
kwh_bac1 = (so_kwh <= 100) * so_kwh + (so_kwh > 100) * 100

# Bậc 2: từ 101 - 200 kWh
kwh_bac2 = (so_kwh > 100) * ((so_kwh <= 200) * (so_kwh - 100) + (so_kwh > 200) * 100)

# Bậc 3: trên 200 kWh
kwh_bac3 = (so_kwh > 200) * (so_kwh - 200)

# Tính tổng tiền
tong_tien = kwh_bac1 * gia_bac1 + kwh_bac2 * gia_bac2 + kwh_bac3 * gia_bac3

# In kết quả
print(f"Tổng số tiền điện phải trả: {tong_tien:.0f} VNĐ")

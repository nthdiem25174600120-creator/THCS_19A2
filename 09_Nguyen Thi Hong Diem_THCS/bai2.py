# Nhập tổng số kẹo và số học sinh từ bàn phím
tong_keo = int(input("Nhập tổng số kẹo: "))
so_hoc_sinh = int(input("Nhập số học sinh: "))
# Tính số kẹo mỗi học sinh nhận được
keo_moi_hs = tong_keo // so_hoc_sinh
# Tính số kẹo còn thừa
keo_thua = tong_keo % so_hoc_sinh
# In kết quả
print(f"Mỗi học sinh nhận được {keo_moi_hs} kẹo")
print(f"Số kẹo còn thừa là {keo_thua}")
# Nhập giá sản phẩm và số lượng mua từ bàn phím 
gia = float(input("Nhập giá sản phẩm: "))
so_luong = int(input("Nhập số lượng mua: "))
# Tính tổng chi phí
tong_chi_phi = gia * so_luong
# Tính VAT (10%)
vat = tong_chi_phi * 0.10
# Tổng tiền phải trả
tong_tien = tong_chi_phi + vat
# In kết quả, làm tròn đến 2 chữ số thập phân
print("Tổng tiền phải trả (đã gồm VAT):", round(tong_tien, 2))
# Nhập số tiền VNĐ từ bàn phím
vnd = float(input("Nhập số tiền VNĐ: "))
# Tỷ giá quy đổi
ty_gia = 24500
# Tính số tiền USD
usd = vnd / ty_gia
# Làm tròn đến 2 chữ số thập phân
usd = round(usd, 2)
# In kết quả
print(f"Số tiền tương đương: {usd} USD")


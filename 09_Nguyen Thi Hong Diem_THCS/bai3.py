# Nhập độ dài cạnh đáy và chiều cao từ bàn phím
day = float(input("Nhập độ dài cạnh đáy (cm): "))
chieu_cao = float(input("Nhập chiều cao (cm): "))
# Tính diện tích tam giác
dien_tich = (day * chieu_cao) / 2
# In kết quả
print(f"Diện tích tam giác là: {dien_tich} cm²")
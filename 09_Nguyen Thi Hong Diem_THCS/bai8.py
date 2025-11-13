# Nhập cân nặng và chiều cao từ bàn phím
can_nang = float(input("Nhập cân nặng (kg): "))
chieu_cao = float(input("Nhập chiều cao (m): "))
# Tính chỉ số BMI theo công thức
bmi = can_nang / (chieu_cao * chieu_cao)
# Làm tròn đến 2 chữ số thập phân
bmi = round(bmi, 2)
# In kết quả
print(f"Chỉ số BMI của bạn là: {bmi}")
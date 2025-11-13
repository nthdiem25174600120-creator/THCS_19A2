# Nhập một năm từ bàn phím
nam = int(input("Nhập một năm: "))

# Tính biểu thức kiểm tra năm nhuận (trả về True hoặc False)
la_nam_nhuan = (nam % 400 == 0) or ((nam % 4 == 0) and (nam % 100 != 0))

# In kết quả  
print("Kết quả kiểm tra năm nhuận là:", la_nam_nhuan)


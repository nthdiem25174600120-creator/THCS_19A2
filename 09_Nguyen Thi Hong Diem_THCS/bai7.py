# Nhập tên đăng nhập và mật khẩu
ten_dang_nhap = input("Nhập tên đăng nhập: ")
mat_khau = input("Nhập mật khẩu: ")

# Kiểm tra quyền truy cập
quyen_truy_cap = (ten_dang_nhap == "admin") and (mat_khau != "password123")

# In kết quả
print("Quyền truy cập:", quyen_truy_cap)

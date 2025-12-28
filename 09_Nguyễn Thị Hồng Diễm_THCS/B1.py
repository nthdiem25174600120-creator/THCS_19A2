noi_dung = ("Python là một ngôn ngữ lập trình mạnh mẽ, dễ học và có nhiều ứng dụng. "
           "Nó được sử dụng rộng rãi trong phát triển web, khoa học dữ liệu, "
           "trí tuệ nhân tạo và tự động hóa. Cộng đồng Python rất lớn và hỗ trợ tuyệt vời, "
           "với nhiều thư viện phong phú để giải quyết mọi vấn đề.")
with open("van_ban.txt", "w", encoding="utf-8") as f:
    f.write(noi_dung)
with open("van_ban.txt", "r", encoding="utf-8") as f:
    data = f.read()
words = data.split()
tong_so_tu = len(words)

print(f"Nội dung đã đọc: \n{data}\n")
print(f" Tổng số từ trong tập tin là: {tong_so_tu}")
danh_sach_so = [1, 2, 3, 4, 5, 10, 15, 20]
with open("so_nguyen.txt", "w", encoding="utf-8") as f:
    for so in danh_sach_so:
        f.write(str(so) + "\n")
print("Đã ghi danh sách số vào file so_nguyen.txt")
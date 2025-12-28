with open("nguon.txt", "rb") as f_nguon, open("dich.txt", "wb") as f_dich:
    while True:
        khoi_du_lieu = f_nguon.read(1024)
        if not khoi_du_lieu:
            break
        f_dich.write(khoi_du_lieu)

print("Đã sao chép tập tin thành công!")

with open("dich.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()

print("\nNội dung trong file đích:")
print(noi_dung)
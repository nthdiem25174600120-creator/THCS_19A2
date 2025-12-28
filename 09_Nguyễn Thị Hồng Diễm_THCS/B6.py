import csv
with open("nhan_vien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Ten", "Luong"])
    writer.writerow([1, "An", 1000])
    writer.writerow([2, "Bình", 1200])
    writer.writerow([3, "Chi", 1500])
with open("nhan_vien.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for dong in reader:
        print("ID:", dong["ID"])
        print("Tên:", dong["Ten"])
        print("Lương:", dong["Luong"])
        print("------")
with open("van_ban.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()
tu_list = noi_dung.split()
dem_tu = {}
for tu in tu_list:
    dem_tu[tu] = dem_tu.get(tu, 0) + 1
print("Số lần xuất hiện của các từ:")
for tu, so_lan in dem_tu.items():
    print(tu, ":", so_lan)

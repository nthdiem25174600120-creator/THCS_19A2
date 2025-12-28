from chuoi_utility import dao_nguoc_chuoi,dem_so_tu
chuoi_ban_dau = "xin chào các bạn"
chuoi_dao_nguoc = dao_nguoc_chuoi(chuoi_ban_dau)
print("chuỗi đảo ngược:", chuoi_dao_nguoc)
so_tu = dem_so_tu(chuoi_ban_dau)
print("số từ trong chuỗi:", so_tu)
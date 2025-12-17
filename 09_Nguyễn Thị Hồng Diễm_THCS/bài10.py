m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
ma_tran = []
for i in range(m):
    dong = input("Nhập hàng thứ " + str(i+1) + " (các số cách nhau bởi khoảng trắng): ")
    hang = []
    so_hien_tai = ""
    for ky_tu in dong:
        if ky_tu != " ":
            so_hien_tai += ky_tu
        else:
            if so_hien_tai != "":
                hang.append(int(so_hien_tai))
                so_hien_tai = ""
    if so_hien_tai != "":
        hang.append(int(so_hien_tai))
    ma_tran.append(hang)
tong_lon_nhat = None
chi_so_hang = -1

for i in range(m):
    tong_hang = 0
    for x in ma_tran[i]:
        tong_hang += x
    if tong_lon_nhat is None or tong_hang > tong_lon_nhat:
        tong_lon_nhat = tong_hang
        chi_so_hang = i
print("Hàng có tổng lớn nhất là hàng thứ", chi_so_hang + 1, "với tổng =", tong_lon_nhat)
print("Nội dung hàng đó:", ma_tran[chi_so_hang])
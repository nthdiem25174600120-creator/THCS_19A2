n = int(input("Nhập kích thước ma trận vuông n: "))
ma_tran = []
for i in range(n):
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

tong = 0
for i in range(n):
    tong += ma_tran[i][n - 1 - i]

print("Tổng các phần tử trên đường chéo phụ là:", tong)
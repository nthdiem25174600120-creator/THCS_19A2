def nhap_ma_tran(so_hang, so_cot):
    ma_tran = []
    for i in range(so_hang):
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
    return ma_tran

m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))

if m != n:
    print("Ma trận không phải ma trận vuông → KHÔNG thể là ma trận đơn vị.")
else:
    print("Nhập ma trận:")
    A = nhap_ma_tran(m, n)

    la_don_vi = True
    for i in range(m):
        for j in range(n):
            if i == j and A[i][j] != 1:
                la_don_vi = False
                break
            elif i != j and A[i][j] != 0:
                la_don_vi = False
                break
        if not la_don_vi:
            break

    if la_don_vi:
        print("Ma trận là ma trận đơn vị.")
    else:
        print("Ma trận KHÔNG phải là ma trận đơn vị.")
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

m = int(input("Nhập số hàng của ma trận A: "))
n = int(input("Nhập số cột của ma trận A: "))
print("Nhập ma trận A:")
A = nhap_ma_tran(m, n)

n2 = int(input("Nhập số hàng của ma trận B: "))
p = int(input("Nhập số cột của ma trận B: "))
print("Nhập ma trận B:")
B = nhap_ma_tran(n2, p)

if n != n2:
    print("Không thể nhân ma trận: số cột A phải bằng số hàng B.")
else:
    C = []
    for i in range(m):
        hang_ket_qua = []
        for j in range(p):
            tong = 0
            for k in range(n):
                tong += A[i][k] * B[k][j]
            hang_ket_qua.append(tong)
        C.append(hang_ket_qua)

    print("Kết quả phép nhân ma trận A x B là:")
    for hang in C:
        for x in hang:
            print(x, end=" ")
        print()
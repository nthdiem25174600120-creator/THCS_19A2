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

doi_xung = True
for i in range(n):
    for j in range(n):
        if ma_tran[i][j] != ma_tran[j][i]:
            doi_xung = False
            break
    if not doi_xung:
        break

if doi_xung:
    print("Ma trận là ma trận đối xứng.")
else:
    print("Ma trận KHÔNG phải là ma trận đối xứng.")
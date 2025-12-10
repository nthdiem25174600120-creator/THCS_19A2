def tinh_trung_binh_cong(a, b, c):
    return (a+b+c)/3
a=int(input("nhập số thứ nhất: "))
b=int(input("nhập số thứ hai: "))
c=int(input("nhập số thứ ba: "))
ket_qua=tinh_trung_binh_cong(a, b, c)
print(f"Trung bình cộng 3 số là: ",ket_qua)

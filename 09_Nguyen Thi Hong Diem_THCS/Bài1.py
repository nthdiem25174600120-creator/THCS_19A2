def chuyen_doi_nhiet_do(do_c):
    return do_c*9/5+32
do_c=int(input("Nhập độ C: "))
do_f=chuyen_doi_nhiet_do(do_c)
print("Chuyển sang độ F là: ",do_f)
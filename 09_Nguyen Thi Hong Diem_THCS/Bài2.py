def giai_phuong_trinh_bac_nhat(a,b):
    if a !=0:
        x=-b/a
        print(f"phương trình {a}x+{b}=0 có nghiệm : x = {x}")
    else:
        if b==0:
            print("phương trình vô số nghiệm.")
        else:
            print("phương trình vô nghiệm")
x =int(input("nhập số a: "))
y =int(input("nhập số b: "))
giai_phuong_trinh_bac_nhat(x,y)
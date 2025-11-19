i = int(input("Nhập i: "))
for n in range(2, i) :
    nguyen_to = True
    for i in range(2, n) :
        if n % i == 0 :
            nguyen_to = False
            break
    if nguyen_to :
            print(n, end= "")
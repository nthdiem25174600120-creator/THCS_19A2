n = int(input("Nhập một số: "))
i = 0
while i * i <= n:
    if i * i == n:
        print(n, "là số chính phương.")
        break
    i += 1
else:
    print(n, "không phải số chính phương.")

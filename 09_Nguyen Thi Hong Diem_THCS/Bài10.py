def tim_so_fibonacci(n):
    if n < 0:
        print("Không hợp lệ: Số Fibonacci chỉ tính cho n >= 0.")
        return 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    return tim_so_fibonacci(n - 1) + tim_so_fibonacci(n - 2)

n_input = int(input("nhập số: "))
ket_qua = tim_so_fibonacci(n_input)
print(f"Số Fibonacci thứ {n_input} là: {ket_qua}") 
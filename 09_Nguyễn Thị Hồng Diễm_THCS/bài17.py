chuoi = input("Nhập các cặp key-value (key là chuỗi, value là số), cách nhau bởi khoảng trắng: ")
ds = []
tam = ""
for ky_tu in chuoi:
    if ky_tu != " ":
        tam += ky_tu
    else:
        if tam != "":
            ds.append(tam)
            tam = ""
if tam != "":
    ds.append(tam)

d = {}
for i in range(0, len(ds), 2):
    key = ds[i]
    value = int(ds[i+1])
    d[key] = value

key_lon_nhat = None
value_lon_nhat = None

for k in d:
    if value_lon_nhat is None or d[k] > value_lon_nhat:
        value_lon_nhat = d[k]
        key_lon_nhat = k

print("Dictionary:", d)
print("Key có giá trị lớn nhất là:", key_lon_nhat, "với giá trị =", value_lon_nhat)
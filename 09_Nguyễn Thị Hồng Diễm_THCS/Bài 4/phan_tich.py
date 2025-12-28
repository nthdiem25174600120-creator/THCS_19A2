from du_lieu.danh_sach import sap_xep_tang_dan
from du_lieu.tu_dien import lay_gia_tri
ds = [5, 2, 9, 1, 7]
print("Danh sách ban đầu:", ds)
print("Danh sách sau khi sắp xếp:", sap_xep_tang_dan(ds))
td = {"ten": "A", "lop": "9B", "truong": "THCS"}
print("Giá trị của khóa 'ten':", lay_gia_tri(td, "ten"))
print("Giá trị của khóa 'tuoi':", lay_gia_tri(td, "tuoi"))



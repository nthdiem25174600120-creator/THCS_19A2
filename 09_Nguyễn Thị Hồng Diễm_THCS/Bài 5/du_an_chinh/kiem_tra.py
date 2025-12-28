import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

sys.path.append(parent_dir)

try:
    from thu_vien_chung import xu_ly_so

    so_can_check = 17
    if xu_ly_so.kiem_tra_so_nguyen_to(so_can_check):
        print(f"{so_can_check} là số nguyên tố")
    else:
        print(f"{so_can_check} không phải là số nguyên tố")
except ImportError:
    print("Lỗi: Hãy đảm bảo thư mục 'thu_vien_chung' nằm đúng vị trí.")

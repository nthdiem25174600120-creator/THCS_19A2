import os
os.makedirs("my_project/src", exist_ok=True)
os.makedirs("my_project/docs", exist_ok=True)
os.makedirs("my_project/data", exist_ok=True)
open("my_project/src/main.py", "w").close()
open("my_project/docs/README.md", "w").close()
open("my_project/data/input.txt", "w").close()
print("Cấu trúc thư mục vừa tạo:")
for thu_muc in os.listdir("my_project"):
    print("-", thu_muc)
    duong_dan = os.path.join("my_project", thu_muc)
    if os.path.isdir(duong_dan):
        for tap_tin in os.listdir(duong_dan):
            print("   +", tap_tin)
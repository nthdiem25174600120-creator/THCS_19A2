import os
os.mkdir("temp_files")
open("temp_files/file.txt", "w").close()
os.rename("temp_files/file.txt", "temp_files/new_file.txt")
os.rename("temp_files/new_file.txt", "new_file.txt")
os.rmdir("temp_files")
print("Hoàn thành các thao tác.")
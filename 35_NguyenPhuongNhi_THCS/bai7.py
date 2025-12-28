import os

os.makedirs("du_lieu/van_ban", exist_ok=True)

open("du_lieu/van_ban/file1.txt", "w").close()
open("du_lieu/van_ban/file2.txt", "w").close()

print("Nội dung thư mục du_lieu:")
print(os.listdir("du_lieu"))

print("Nội dung thư mục van_ban:")
print(os.listdir("du_lieu/van_ban"))

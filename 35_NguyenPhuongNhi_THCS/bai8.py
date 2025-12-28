import os

os.mkdir("temp_files")

with open("temp_files/file.txt", "w") as f:
    f.write("File tam")

os.rename("temp_files/file.txt", "temp_files/new_file.txt")

os.rename("temp_files/new_file.txt", "new_file.txt")

os.rmdir("temp_files")

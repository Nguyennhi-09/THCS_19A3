import csv

with open("nhan_vien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Tên", "Lương"])
    writer.writerow(["1", "An", "45000"])
    writer.writerow(["2", "Bình", "60000"])
    writer.writerow(["3", "Chi", "75000"])
    writer.writerow(["4", "Dũng", "50000"])

with open("nhan_vien.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    print("Nhân viên có lương trên 50000:")
    for dong in reader:
        if int(dong["Lương"]) > 50000:
            print("ID:", dong["ID"], "- Tên:", dong["Tên"], "- Lương:", dong["Lương"])

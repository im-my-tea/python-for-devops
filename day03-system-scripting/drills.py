import os
import shutil

fp = "messy_folder"
f = os.listdir(fp)
print(f"Files found: {f}")

lf = os.path.join("messy_folder", "logs")
if not os.path.exists(lf):
    os.mkdir(lf)
    print("Log folder created.")
else:
    print("Log folder already exists.")


src =  os.path.join("messy_folder", "file_0.txt")
dst = os.path.join(lf, "file_0.txt")
try:
    shutil.move(src, dst)
    print("Moved file_0.txt to logs.")
except FileNotFoundError:
    print("File not found (maybe already moved?)")

print(f"Files found: {f}")
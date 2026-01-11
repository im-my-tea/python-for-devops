import os
import shutil

file_path = "messy_folder"
files = os.listdir(file_path)

for file in files:
    src = os.path.join(file_path, file)

    if os.path.isdir(src):
        continue

    _, ext = os.path.splitext(file)

    dstf = ""
    if ext == ".txt":
        dstf = "Logs"
    elif ext == ".jpg":
        dstf = "Images"
    else:
        continue

    dst = os.path.join(file_path, dstf)

    if not os.path.exists(dst):
        os.mkdir(dst)
        print(f"Created folder: {dst}")

    findst = os.path.join(dst, file)

    try:
        shutil.move(src, findst)
        print(f"Moved: {file} -> {dstf}/")
    except Exception as e:
        print(f"Error moving {file}: {e}")
        
print("Cleanup Complete!")
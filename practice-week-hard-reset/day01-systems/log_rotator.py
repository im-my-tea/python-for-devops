import os
import time
import zipfile
from datetime import datetime

SOURCE_DIR = "server_logs"
BACKUP_DIR = "backups"
MAX_SIZE = 100 * 1024



def get_folder_size(folder):
    total = 0 
    for f in os.listdir(folder):
        path = os.path.join(folder, f)
        total += os.path.getsize(path)
    return total


def perform_rotation():
    print("--- Starting Rotation ---")
    
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name = os.path.join(BACKUP_DIR, f"logs_{timestamp}.zip")
    files_to_archive = os.listdir(SOURCE_DIR)

    with zipfile.ZipFile(zip_name, 'w') as f:
        for file in files_to_archive:
            file_path = os.path.join(SOURCE_DIR, file)
            f.write(file_path, arcname=file)
    print(f"Archived {len(files_to_archive)} files to {zip_name}")

    for file in files_to_archive:
        os.remove(os.path.join(SOURCE_DIR, file))
    print("Original logs cleaned.")    




print(f"Monitoring {SOURCE_DIR} for size limit {MAX_SIZE} bytes...")

while True:
    size = get_folder_size(SOURCE_DIR)
    print(f"Current size: {size} bytes")

    if size > MAX_SIZE:
        print("⚠️ Limit exceeded! Rotating...")
        perform_rotation()

    time.sleep(5)
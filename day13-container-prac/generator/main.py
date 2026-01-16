import os
import time
from datetime import datetime

# 1. Define the shared path
LOG_PATH = "/shared_data/secret_logs.txt"
LOG_DIR = "/shared_data"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

print("--- GENERATOR STARTED ---")

while True:
    # 2. Create timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] SECRET DATA: System is running.\n"
    
    # 3. Append to file
    with open(LOG_PATH, "a") as f:
        f.write(entry)
    
    print(f"Written: {entry.strip()}")
    
    # 4. Wait
    time.sleep(5)
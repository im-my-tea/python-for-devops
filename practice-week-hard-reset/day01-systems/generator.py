import os
import time
import random

LOG_DIR = "server_logs"
if os.path.exists(LOG_DIR):
    print("Directory already exists!")
else:
    os.makedirs(LOG_DIR)

print("--- CHAOS GENERATOR STARTED ---")

while True:
    data = "ERROR: Connection Timeout 505 " * 1000
    name = f"log_{int(time.time())}_{random.randint(1,100)}.txt"
    path = os.path.join(LOG_DIR, name)

    with open(path, 'w') as f:
        f.write(data)
    
    print(f"Generated {name}!")
    time.sleep(1)
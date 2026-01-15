import redis
import time
import os

# --- CONFIGURATION ---
# We will define these variables inside docker-compose.yaml tomorrow
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

print(f"--- Connecting to Redis at {REDIS_HOST}:{REDIS_PORT} ---")

def run_app():
    # Logic to connect and count hits goes here tomorrow
    pass

if __name__ == "__main__":
    while True:
        run_app()
        time.sleep(5)
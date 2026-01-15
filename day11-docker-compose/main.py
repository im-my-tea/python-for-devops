import redis
import time
import os
import sys

# 1. Configuration (Env variables from Docker)
# Note: "redis" is the hostname we will define in docker-compose.yaml
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# 2. Connect to Database
try:
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
except Exception as e:
    print(f"Error connecting to Redis: {e}")
    sys.exit(1)

def run_app():
    while True:
        try:
            # 3. Database Logic: Increment 'hits' key
            hits = r.incr('hits')
            print(f"Hello Cloud! I have been seen {hits} times.")
            time.sleep(5)
        except redis.ConnectionError:
            print("Waiting for Redis...")
            time.sleep(5)

if __name__ == "__main__":
    print("--- Starting App ---")
    run_app()
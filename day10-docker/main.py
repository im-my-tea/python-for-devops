import requests
import time
import os

# Get URL from Environment Variable (we will inject this via Docker later)
TARGET_URL = os.getenv("TARGET_URL", "https://www.google.com")

def check_status():
    print(f"--- Monitoring: {TARGET_URL} ---")
    try:
        response = requests.get(TARGET_URL)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("✅ Site is Online")
        else:
            print(f"⚠️ Issue Detected: {response.status_code}")
    except Exception as e:
        print(f"❌ Connection Failed: {e}")

if __name__ == "__main__":
    while True:
        check_status()
        print("Sleeping for 5 seconds...")
        time.sleep(5)
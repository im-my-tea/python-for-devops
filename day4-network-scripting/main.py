import requests
from datetime import datetime

# 1. The Targets (Real and Fake sites)
urls = [
    "https://www.google.com",
    "https://github.com",
    "https://httpstat.us/404",      # Simulates a missing page
    "https://httpstat.us/500",      # Simulates a server crash
    "https://thisdomaindoesnotexist12345.com" # Simulates a DNS failure
]

def log_error(url, message):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    with open("downtime.log", 'a') as f:
        f.write(f"{timestamp} | ERROR: {message} | URL: {url}\n")


print("--- Starting System Monitor ---")


for i in urls:
    try:
        r = requests.get(i)
        if r.status_code == 200:
            print(f"[✅ ONLINE] {i}")
        elif r.status_code == 404:
            print(f"[❌ 404 NOT FOUND] {i}")
            log_error(i, "404 Not Found")
        elif r.status_code >= 500:
            print(f"[🔥 500 SERVER ERROR] {i}")
            log_error(i, "500 Server Error")
    except requests.exceptions.ConnectionError:
        print(f"[☠️ DEAD] {i}")
        log_error(i, "DNS/Connection Failed")


print("--- Check Complete ---")
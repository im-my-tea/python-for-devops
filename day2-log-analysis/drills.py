sample_log = "2024-01-15 10:05:23 - ERROR - Connection refused"
sample = sample_log.split(" - ")
print(f"Timestamp - {sample[0]} \nError - {sample[1]} \nMessage - {sample[2]} ")

attack_log = "2024-01-15 10:15:00 - ERROR - Root access attempted from 45.33.22.11"
attack = attack_log.split(" ")
ip = attack[-1]
print(f"IP - {ip}")

with open("server.log", "r") as f:
    for line in f:
        if "ERROR" in line:
            parts = line.split(" - ")
            print(f"Alert: {parts[2].strip()}")

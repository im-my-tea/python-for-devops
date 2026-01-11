ip_counts = {}

with open("server.log", 'r') as f:
    for line in f:
        if "ERROR" in line:
            x = line.split(" ")
            ip = x[-1].strip()
            if ip in ip_counts:
                ip_counts[ip] += 1
            else: 
                ip_counts[ip] = 1

with open("suspicious_ips.csv", 'w') as f:
    f.write("IP Address: Count\n\n")
    for i,j in ip_counts.items():
        f.write(f"{i} - {j}\n")

print("Report Generated!")


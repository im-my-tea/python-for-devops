from inventory import servers

print(servers[1]["ip"])
print(servers[-1]["region"])
print(servers[3]["cpu_usage"])

for s in servers:
    print(f"Hostname: {s['hostname']} | IP: {s['ip']} | Region: {s['region']}")

high_load = []
for s in servers:
    if s['cpu_usage'] > 50:
        high_load.append(s['hostname'])
print(high_load)
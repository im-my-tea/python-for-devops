from inventory import servers


CPU = 0
HCPU = 0
for s in servers:
    CPU += s['cpu_usage']
    if s['cpu_usage'] > HCPU:
        H = s
        HCPU = s['cpu_usage']
    if s['status'] == "running" and s['cpu_usage'] == 0:
        print(f"WARNING: Server {s['hostname']} is idle. Consider stopping.")
    


print(f"Average CPU Load: {CPU/len(servers)}")
print(f"ALERT: Server {H['hostname']} is overloaded! Load: {HCPU}%")

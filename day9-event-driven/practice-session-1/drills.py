aws_logs = [
    {"id": 1, "metadata": {"ip": "10.0.0.1", "status": "OK"}},
    {"id": 2, "metadata": {"ip": "10.0.0.2", "status": "CRITICAL"}},
    {"id": 3, "metadata": {"ip": None, "status": "CRITICAL"}}, # Trap! No IP
    {"id": 4, "metadata": {"ip": "10.0.0.4", "status": "WARNING"}}
]

def parse_cloud_log(data):
    critical = []
    for log in data:
        s = log['metadata']['status']
        ip = log['metadata']['ip']
        if s == "CRITICAL" and ip != None:
            critical.append(log['metadata'])
    print(f"IPs with Warning: {critical}")

parse_cloud_log(aws_logs)

import os

def backup():
    folder = "logs_backup"
    os.makedirs(folder, exist_ok=True)

    for i in range(5):
        file = f"server_{i}.log"
        path = os.path.join(folder, file)

        with open(path, 'w') as f:
            f.write("System OK!")

    print(f"Created files in {folder}: ")
    print(os.listdir(folder))

backup()
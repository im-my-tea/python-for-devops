from inventory import servers


print(" 1. List Fleet " \
    "2. Count Running Servers " \
    "3. Stop a Server " \
    "0. Exit ")


while True:
    choice = int(input("Enter Choice: "))
    if choice == 0:
        print("Exiting! Bye!")
        break
    elif choice == 1:
        for s in servers:
            print(f"Hostname: {s['hostname']} | IP: {s['ip']} | Region: {s['region']} | Status: {s['status']}")
    elif choice == 2:
        C = 0
        for s in servers:
            if s["status"] == "running":
                C += 1
        print(f"Number of Running Servers: {C}")
    elif choice == 3:
        S = input("Which server to stop? (hostname): ")
        C = 0
        for s in servers:
            if s["hostname"] == S:
                s["status"] = 'stopped'
                C += 1
                print(f"{s["hostname"]} stopped!")
        if C == 0:
            print("Server does NOT exist!")
    else:
        print("Wrong choice! Choose again!")
        continue


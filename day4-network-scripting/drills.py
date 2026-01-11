import requests

r1 = requests.get("https://www.google.com")
if r1.status_code == 200:
    print("Google is up!")
else:
    print(f"Google is Down! Status: {r1.status_code}")

r2 = requests.get("https://jsonplaceholder.typicode.com/users/1")
d2 = r2.json()
print(f"User {d2['name']} lives in {d2['address']['city']}!")


try:
    r3 = requests.get("https://thisisnotawebsite.xyz")
except requests.exceptions.ConnectionError: 
    print("DNS Error: Domain not found.")
import json
import hashlib
import os
import sys

# Constants
DB_FILE = "users.json"

class User:
    def __init__(self, username, pin, balance=0):
        self.username = username
        self.pin_hash = hashlib.sha256(pin.encode()).hexdigest()
        self.balance = balance

    
    def check_pin(self, input_pin):
        input_hash = hashlib.sha256(input_pin.encode()).hexdigest()
        return input_hash == self.pin_hash
    
    def to_dict(self):
        return {
            'username':self.username,
            'pin_hash':self.pin_hash,
            'balance':self.balance
        }
    

class BankSystem:
    def __init__(self):
        self.users = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(DB_FILE):
            try:
                with open(DB_FILE, 'r') as f:
                    self.users = json.load(f)
            except json.JSONDecodeError:
                self.users = {}

    def save_data(self):
        with open(DB_FILE, 'w') as f:
            json.dump(self.users, f, indent=4)

    def create_account(self, username, pin):
        if username in self.users:
            print("User already exists!")
            return False
        # Create User Object
        new_user = User(username, pin)
        # Store dictionary version
        self.users[username] = new_user.to_dict()
        self.save_data()
        print(f"Account created for {username}.")
        return True

    def login(self, username, pin):
        if username not in self.users:
            return None
        # Get data from dict
        user_data = self.users[username]
        stored_hash = user_data['pin_hash']
        # Check PIN
        input_hash = hashlib.sha256(pin.encode()).hexdigest()
        if input_hash == stored_hash:
            # Reconstruct User Object
            return User(username, pin, user_data['balance'])
        else:
            return None


bank = BankSystem()
bank.create_account("Jack", "9999")
user = bank.login("Jack", "9999")
if user:
    print(f"Logged in as {user.username}. Balance: {user.balance}")
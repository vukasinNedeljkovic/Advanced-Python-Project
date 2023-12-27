import hash
import time
import multiprocessing

registered_users = {}  
logged_in_users = []

import hash

class User:
    def __init__(self, username, password):
        self._username = username
        self._password = self.validate_password(password)
        self._contacts = []

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = self.validate_password(value)

    @property
    def contacts(self):
        return self._contacts

    @contacts.setter
    def contacts(self, contact):
        self._contacts.append(contact)

    @contacts.deleter
    def contacts(self):
        if self._contacts:
            del self._contacts[-1]

    def validate_password(self, password):
        if len(password) <= 12 and password.isdigit():
            return hash.hash_password(password)
        else:
            raise ValueError("The password can have a maximum of 12 characters")

    def __len__(self):
        return len(self._contacts)

    def __str__(self):
        return f"Username: {self._username}, Contacts: {[contact for contact in self._contacts]}"

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self._contacts):
            result = self._contacts[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration


def register(username, password):
    if username in registered_users:
        print("Username already exists. Please choose another username.")
        return None

    new_user = User(username, password)
    registered_users[username] = new_user
    return new_user

def simulate_login(username):
        time.sleep(1)
        print(f"User {username} is logged in.")

def login(username, password):

    if username not in registered_users:
        print("User is not registered. Please register first.")
        return
    
    stored_user = registered_users[username]
    stored_hashed_password = stored_user.password

    if stored_hashed_password != hash.hash_password(password):
        print("Invalid password. Please try again.")
        return

    logged_in_users.append(username)

    process = multiprocessing.Process(target=simulate_login, args=(username,))
    process.start()

def logout(username):
    if username in logged_in_users:
        logged_in_users.remove(username)
        print(f"User {username} has been logged out.")
    else:
        print(f"User {username} is not logged in.")

def add_contact(username, contact):
    if username in logged_in_users:
        registered_users[username].contacts = contact
        print(f"Contact '{contact}' added for user '{username}'.")
    else:
        print(f"User {username} is not logged in. Please log in first.")

def remove_contact(username):
    if username in logged_in_users:
        user = registered_users[username]

        if len(user.contacts) > 0:
            contact = user.contacts[-1]
            del user.contacts
            print(f"Contact '{contact}' removed for user '{username}'.")
        else:
            print(f"User '{username}' does not have contacts to remove")
    else:
        print(f"User {username} is not logged in. Please log in first.")

def print_contact(username):
    if username in logged_in_users:
        user = registered_users[username]
        print(f"Contacts for user '{username}':")
        contacts_iter = iter(user)

        try:
            index = 0
            while True:
                contact = next(contacts_iter)
                print(f"[{index}] {contact}")
                index += 1
        except StopIteration:
            pass
    else:
        print(f"User {username} is not logged in. Please log in first.")


    
    
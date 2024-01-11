import hash
import time
import multiprocessing

from user_management_lib.user import *

registered_users = {}  
logged_in_users = []

def register(username, password):
    if username in registered_users:
        print("Username already exists. Please choose another username.")
        return None

    if len(password) <= 12 and password.isdigit():
        hashed_password = hash.hash_password(password)
        new_user = User(username, hashed_password)
        registered_users[username] = new_user
        return new_user
    else:
        raise ValueError("The password can have a maximum of 12 characters and must be a digit")
    
def simulate_login(username):
        time.sleep(1)
        print(f"User {username} is logged in.")

def login(username, password):
    if username not in registered_users:
        print("User is not registered. Please register first.")
        return
    
    if username in logged_in_users:
        print("User is already logged in.")
        return
    
    stored_user = registered_users[username]
    stored_hashed_password = stored_user.password

    if hash.check_password(password, stored_hashed_password):
        print("Invalid password. Please try again.")
        return

    logged_in_users.append(username)

    process = multiprocessing.Process(target=simulate_login, args=(username,))
    process.start()
    process.join()

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


    
    


    
    
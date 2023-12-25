import hash
from user import *
import time
import multiprocessing

registered_users = {}  
logged_in_users = []


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

def check_user_logged_in(username):
    return username in logged_in_users

def get_user_by_username(username):
    return [user for user in registered_users if user.username == username]
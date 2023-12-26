from user import *
from functions import *


def display_menu():
    print("Welcome to User management")
    print("1. Register")
    print("2. Login")
    print("3. Add contact")
    print("4. Remove contact")
    print("5. Print contact")
    print("6. Logout")
    print("7. Exit")
    time.sleep(2)
    choice = input("Enter your choice: ")
    return choice.strip()

def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = register(username, password)
    if user:
        print("Registration successful.")

def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    login(username, password)

def add_contact_input():
    username = input("Enter username: ")
    contact = input("Enter contact: ")
    add_contact(username, contact)

def remove_contact_input():
    username = input("Enter username: ")
    remove_contact(username)

def print_contact_input():
    username = input("Enter username: ")
    print_contact(username)

def logout_user():
    username = input("Enter username to logout: ")
    logout(username)


def main():
    while True:
        choice = display_menu()
        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            add_contact_input()
        elif choice == '4':
            remove_contact_input()
        elif choice == '5':
            print_contact_input()
        elif choice == '6':
            logout_user()
        elif choice == '7':
            print("Exiting the User Authentication System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

    #user = User("User", "123")
    #user1 = User("User1", "123")
    #user2 = User("User2", "123")
    #user.contacts = user1
    #user.contacts = user2

    #print(user.username)
    #print(user.password)
    #print(user)


    #iterrator = iter(user)
    #try:
        #while True:
            #print(next(iterrator))
    #except StopIteration:
        #print('Done')
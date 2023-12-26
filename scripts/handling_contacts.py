import user_menagment


def add_contact(username, contact):
    if not user_menagment.check_user_logged_in(username):
        print("User is not logged in")
        return

    user = user_menagment.get_user_by_username(username)
    user.contacts = contact
    print("Contact added")

def remove_contact(username):
    if not user_menagment.check_user_logged_in(username):
        print("User is not logged in")
        return

    user = user_menagment.get_user_by_username(username)
    if len(user.contacts) > 0:
        del user.contacts
        print("Contact removed")
    else:
        print("User does not have contacts to remove")

def print_contact(username):
    if not user_menagment.check_user_logged_in(username):
        print("User is not logged in")
        return

    user = user_menagment.get_user_by_username(username)
    contacts_iter = iter(user)

    try:
        index = 0
        while True:
            contact = next(contacts_iter)
            print(f"[{index}] {contact}")
            index += 1
    except StopIteration:
        pass

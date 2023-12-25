import user_menagment


def add_contact(user, contact):
    if not user in user_menagment.logged_in_users:
        raise Exception("User is not logged in")
    
    user.contacts = contact

def remove_contact(user):
    if not user in user_menagment.logged_in_users:
        raise Exception("User is not logged in")
    
    del user.contacts

def print_contact(user):
    if not user in user_menagment.logged_in_users:
        raise Exception("User is not logged in")
    
    contacts_iter = iter(user)

    try:
        index = 0
        while True:
            contact = next(contacts_iter)
            print("[%d] %s", index, contact)
            index += 1
    except StopIteration:
        pass

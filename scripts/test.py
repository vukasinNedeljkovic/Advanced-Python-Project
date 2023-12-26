import unittest
from user import *
from functions import *

from unittest.mock import patch, MagicMock


class User_management_test_class(unittest.TestCase):

    # Create user with valid username/password
    def create_user_valid(self):
        pass

    # Create user with invalid password
    def create_user_invalid_pass(self):
        pass

    # Getter/setter for username
    def getter_setter_username(self):
        pass

    # Getter/setter for password
    def get_set_password(self):
        pass

    # Getter/setter/deleter for contact
    def get_set_del_contact(self):
        pass

    # length method
    def lenght_method(self):
        pass

    # str method
    def str_method(self):
        pass

    # iterator
    def iterator_test(self):
        pass

    # Register with valid params
    def register_valid(self):
        pass

    # Register with invalid params
    def register_invalid(self):
        pass
    
    # Login with valid params
    def login_valid(self):
        pass

    # Login with invalid params
    def login_invalid(self):
        pass

    # Login with non existing user
    def login_non_exist(self):
        pass

    # Logout
    def logout_test(self):
        pass

    # Logout with user that is not logged in
    def logout_not_logged_in(self):
        pass

    # Add contact valid
    def add_contact_valid(self):
        pass

    # Add contact with user that is not logged in
    def add_contact_not_logged_user(self):
        pass

    # Remove contact valid
    def remove_contact_valid(self):
        pass

    # Remove contact, user not logged in
    def remove_contact_not_logged_user(self):
        pass

    # Print contact
    def print_contacts(self):
        pass

    # Print contact, user not logged in
    def print_contacts_not_logged_user(self):
        pass


if __name__ == '__main__':
    unittest.main()
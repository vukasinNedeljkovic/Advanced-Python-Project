import unittest
from user import *
from functions import *
import hash

from unittest.mock import patch, MagicMock


class User_management_test_class(unittest.TestCase):

    # Create user with valid username/password
    @patch('hash.hash_password')
    def test_create_user_valid(self, mock_hash_password):
        username = "User1"
        password = "123456789"
        mock_hash_password.return_value = 'hashed pass'

        user = User(username, password)
        self.assertEqual(user.username, username)
        self.assertEqual(user.password, 'hashed pass')
        self.assertEqual(len(user.contacts), 0)


    # Create user with invalid password
    @patch('hash.hash_password')
    def test_create_user_invalid_pass(self, mock_hash_password):
        username = "User1"
        password = "12345678901234"
        mock_hash_password.return_value = 'hashed pass'

        with self.assertRaises(ValueError):
            User(username, password)

    # Getter/setter for username
    def test_getter_setter_username(self):
        username = "User1"
        password = "123456789"

        user = User(username, password)

        self.assertEqual(user.username, username)

        new_username = "user1"
        user.username = new_username
        self.assertEqual(user.username, new_username)

    # Getter/setter for password
    @patch('hash.hash_password')
    def test_get_set_password(self, mock_hash_password):
        username = "User1"
        password = "123456789"
        mock_hash_password.return_value = 'hashed pass'

        user = User(username, password)

        self.assertEqual(user.password, 'hashed pass')
        
        new_password = "1234567890"
        mock_hash_password.return_value = 'hashed pass2'
        user.password = new_password
        self.assertEqual(user.password, 'hashed pass2')

    # Getter/setter/deleter for contact
    def test_get_set_del_contact(self):
        user1 = User("user1", "12345")
        user2 = User("user2", "12345")
        user3 = User("user3", "12345")

        user1.contacts = user2
        self.assertEqual(len(user1.contacts), 1)
        self.assertEqual(user1.contacts[0], user2)
        
        user1.contacts = user3
        self.assertEqual(len(user1.contacts), 2)

        self.assertIn(user2, user1.contacts)
        self.assertIn(user3, user1.contacts)

        del user1.contacts
        self.assertEqual(len(user1.contacts), 1)

    # length method
    def test_lenght_method(self):
        user1 = User("user1", "12345")
        user2 = User("user2", "12345")
        user3 = User("user3", "12345")
        
        self.assertEqual(len(user1), 0)
        user1.contacts = user2
        self.assertEqual(len(user1), 1)
        user1.contacts = user3
        self.assertEqual(len(user1), 2)

    # str method
    def test_str_method(self):
        user1 = User("user1", "12345")
        user2 = User("user2", "12345")
        user3 = User("user3", "12345")

        self.assertEqual(str(user1), "Username: user1, Contacts: []")
        user1.contacts = user2
        self.assertEqual(str(user1), "Username: user1, Contacts: ['user2']")
        user1.contacts = user3
        self.assertEqual(str(user1), "Username: user1, Contacts: ['user2', 'user3']")

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
import unittest
import io
import sys

from user import *
from functions import *
import hash

from unittest.mock import patch, MagicMock


class User_management_test_class(unittest.TestCase):

    def setUp(self):
        registered_users.clear()
        logged_in_users.clear()

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput


    def tearDown(self):
        sys.stdout = sys.__stdout__

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

        user1.contacts = "user2"
        self.assertEqual(len(user1.contacts), 1)
        self.assertEqual(user1.contacts[0], "user2")
        
        user1.contacts = "user3"
        self.assertEqual(len(user1.contacts), 2)

        self.assertIn("user2", user1.contacts)
        self.assertIn("user3", user1.contacts)

        del user1.contacts
        self.assertEqual(len(user1.contacts), 1)

    # length method
    def test_lenght_method(self):
        user1 = User("user1", "12345")
        
        self.assertEqual(len(user1), 0)
        user1.contacts = "user2"
        self.assertEqual(len(user1), 1)
        user1.contacts = "user3"
        self.assertEqual(len(user1), 2)

    # str method
    def test_str_method(self):
        user1 = User("user1", "12345")

        self.assertEqual(str(user1), "Username: user1, Contacts: []")
        user1.contacts = "user2"
        self.assertEqual(str(user1), "Username: user1, Contacts: ['user2']")
        user1.contacts = "user3"
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
    def test_logout_not_logged_in(self):
        logged_in_users.append("User1")
        logged_in_users.append("User2")
        logged_in_users.append("User3")

        logout("User4")

        self.assertEqual(3, len(logged_in_users))

    # Add contact valid
    def test_add_contact_valid(self):
        user = User("User1", "123")
        contact1 = "Marko"
        contact2 = "Jovana"
        registered_users[user.username] = user
        logged_in_users.append(user.username)
        
        self.assertEqual(0, len(user.contacts))

        add_contact(user.username, contact1)

        self.assertEqual(1, len(user.contacts))
        self.assertEqual(contact1, user.contacts[0])

        add_contact(user.username, contact2)

        self.assertEqual(2, len(user.contacts))
        self.assertEqual(contact2, user.contacts[1])

    # Add contact with user that is not logged in
    def test_add_contact_not_logged_user(self):
        user = User("User1", "123")
        contact = "Marko"
        registered_users[user.username] = user
        
        self.assertEqual(0, len(user.contacts))

        add_contact(user.username, contact)

        self.assertEqual(0, len(user.contacts))

    # Remove contact valid
    def test_remove_contact_valid(self):
        user = User("User1", "123")
        contact1 = "Marko"
        contact2 = "Jovana"
        user.contacts = contact1
        user.contacts = contact2
        registered_users[user.username] = user
        logged_in_users.append(user.username)
        
        self.assertEqual(2, len(user.contacts))

        remove_contact(user.username)

        self.assertEqual(1, len(user.contacts))
        self.assertEqual(contact1, user.contacts[0])

        remove_contact(user.username)

        self.assertEqual(0, len(user.contacts))

    # Remove contact, user not logged in
    def test_remove_contact_not_logged_user(self):
        user = User("User1", "123")
        contact1 = "Marko"
        contact2 = "Jovana"
        user.contacts = contact1
        user.contacts = contact2
        registered_users[user.username] = user
        
        self.assertEqual(2, len(user.contacts))

        remove_contact(user.username)

        self.assertEqual(2, len(user.contacts))

    # Print contact
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_contacts(self, mock_stdout):
        user = User("User1", "123")
        contact1 = "Marko"
        contact2 = "Jovana"
        user.contacts = contact1
        user.contacts = contact2
        registered_users[user.username] = user
        logged_in_users.append(user.username)
        expected_output = "Contacts for user '" + user.username + "':\n[0] Marko\n[1] Jovana\n"

        print_contact(user.username)
     
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # Print contact, user not logged in
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_contacts_not_logged_user(self, mock_stdout):
        username = "User4"
        expected_output = "User " + username + " is not logged in. Please log in first.\n"

        print_contact(username)
     
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
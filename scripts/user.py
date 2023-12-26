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

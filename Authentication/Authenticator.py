from user_salts import uuid
# verify input
class Authenticator():
    def __init__(self, hashlib, salt):
        self.hashlib = hashlib
        self.salt = salt

    def hash_input(self, hash_i):
        hash_o = self.hashlib.sha256(hash_i)
        return hash_o

    def hash_salt_input(self, hash_i, salt_i):
        hash_salt_i = hash_i + salt_i
        hash_salt_o = self.hashlib.sha256(hash_salt_i)
        return hash_salt_o

    def get_stored_hash(self, called_item):
        # look up in stored hash table
        stored_hash = called_item
        return stored_hash

    def generate_salt(self):
        return 0

    def get_salt(self, username):
        for user in uuid:
            if user[0] == username:
                return user[0]
            else:
                return self.generate_salt()

    def compare_hash(self, called_item, generated_hash):
        stored_hash = self.get_stored_hash(called_item)
        if stored_hash == generated_hash:
            return True
        else:
            # log login attempt
            return False

    def auth_logins(self, username, password, SQL_db):
        salt = self.get_salt(username, SQL_db)
        hs_attempt = self.hash_salt_input(password, salt)
        authentication = self.compare_hash(username, hs_attempt)
        return authentication
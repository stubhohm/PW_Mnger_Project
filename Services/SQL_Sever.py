class SQLSever:
    class_name = "SQLSever"
    class_id = 1

    def __init__(self, sqlite3, random, hashlib, IP = None):
        self.sqlite3 = sqlite3
        self.random = random
        self.hashlib = hashlib
        self.IP = IP
        self.connection = sqlite3.connect('password_database.db')
        self.cursor = self.connection.cursor()
        

    def instane_method(self):
        print('This returns something specific to the instance of the class')

    def class_metho(cls):
        print('This returns something that applies to the whole class')

    def static_method():
        print('This returns something that always returns specific output')

    
    def get_salt(self, username):
        # Perform SQL query to get password salt
        salt = username
        return salt
    
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
        key_length = 16
        random_key = self.random.range(0,9)
        for i in range(key_length):
            random_digit = self.random.range(0,9)
            random_key = (random_key *10) + random_digit

    def compare_hash(self, stored_hash, generated_hash):
        if stored_hash == generated_hash:
            return True
        else:
            # log login attempt
            return False

    def get_cypher_text(self, username):
        a = 0

def main():
    a = 0

if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: SQL_Sever"
    )
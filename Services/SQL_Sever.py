path = 'password_database.db'
credential_table = 'UserCredentials'
passwords_table = 'UserPasswords'
un_sql = 'username'
salt_sql = 'salt'
hashed_pass_sql = 'hashed_password'
user_id_sql = 'user_id'
other_un_sql = 'other_username'
other_pass_sql = 'other_password'

class SQLSever:
    class_name = 'SQLSever'
    class_id = 1

    def __init__(self, sqlite3, random, hashlib, secrets, IP = None):
        self.sqlite3 = sqlite3
        self.random = random
        self.hashlib = hashlib
        self.secrets = secrets
        self.IP = IP
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()
        

    def instane_method(self):
        print('This returns something specific to the instance of the class')

    def class_metho(cls):
        print('This returns something that applies to the whole class')

    def static_method():
        print('This returns something that always returns specific output')

    def get_salt(self, username):
        # Perform SQL query to get password salt
        self.cursor.execute(f'SELECT {salt_sql} FROM {credential_table} WHERE {un_sql} = ?', (username,))
        results = self.cursor.fetchone()[0]
        return results
    
    def hash_input(self, hash_i):
        hash_o = self.hashlib.sha256(hash_i)
        return hash_o

    def hash_salt_input(self, hash_i, salt_i):
        hash_salt_i = hash_i + salt_i
        hash_salt_o = self.hashlib.sha256(hash_salt_i.encode('utf-8'))
        return hash_salt_o.hexdigest()

    def get_stored_hash(self, username):
        # look up in stored hash table
        self.cursor.execute(f'SELECT {hashed_pass_sql} FROM {credential_table} WHERE {un_sql} = ?', (username,))
        results = self.cursor.fetchone()[0]
        return results

    def generate_salt(self):
        key_length = 16
        salt_bytes = self.secrets.token_bytes(key_length)
        salt = ''.join(format(byte, "02x") for byte in salt_bytes)
        return salt

    def compare_hash(self, stored_hash, generated_hash):
        if stored_hash == generated_hash:
            return True
        else:
            # log login attempt
            return False

    def init_data_tables(self):
        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {credential_table} (
                            id INTEGER PRIMARY KEY,
                            {un_sql} TEXT NOT NULL,
                            {salt_sql} TEXT NOT NULL,
                            {hashed_pass_sql} TEXT NOT NULL
            )
            ''')
        
        self.cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {passwords_table} (
            id INTEGER PRIMARY KEY,
            {user_id_sql} INTEGER NOT NULL,
            {other_un_sql} TEXT NOT NULL,
            {other_pass_sql} TEXT NOT NULL,
            FOREIGN KEY ({user_id_sql}) REFERENCES {credential_table}(id)
        )
        ''')

        self.connection.commit()


    def get_cypher_text(self, username):
        self.connection.commit()

    def unique_username(self, username):
        self.cursor.execute(f'SELECT COUNT(*) FROM {credential_table} WHERE {un_sql} = ?', (username,))
        results = self.cursor.fetchone()
        return results is not None and results[0]>0

    def add_user(self, user):
        salt = self.generate_salt()
        hashed_salted_pass = self.hash_salt_input(user.password, salt)
        self.cursor.execute(f'''
            INSERT INTO {credential_table} ({un_sql}, {salt_sql}, {hashed_pass_sql})
            VALUES (?, ?, ?)
            ''',(user.username, salt, hashed_salted_pass))

def main():
    a = 0

if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: SQL_Sever"
    )
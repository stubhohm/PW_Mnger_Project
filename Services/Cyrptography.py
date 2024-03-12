# decyprt data, my implimentation of AES that will have internal hash for security
# and to verify that the implimentation is uncompromised

class Cryptography():
    class_name = "Cryptography"
    class_id = 5
    def __init__(self,
                 secrets,
                 hashlib,
                 random,
                 Cipher,
                 algos,
                 modes,
                 default_backend,
                 key = None):
        self.secrets = secrets
        self.hashlib = hashlib
        self.random = random
        self.Cipher = Cipher
        self.algos = algos
        self.modes = modes
        self.default_backend = default_backend
        self.key = key

    def generate_encryption_key(self, user, salt, keylength=32, iteration=100000,):
        data = (user.username + salt + user.password).encode('utf-8')
        self.key = self.hashlib.pbkdf2_hmac('sha256', data, salt.encode('utf-8'), iteration, keylength)

    def generate_session_id(self, user, authenticator):
        key_length = 16
        random_key = self.random.randrange(0,9)
        self.start_session = True
        for i in range(key_length):
            random_digit = self.random.randrange(0,9)
            random_key = (random_key *10) + random_digit
        hashed_un = self.hashlib.sha256(user.username.encode('utf-8')).digest()
        hashed_rk = self.hashlib.sha256(str(random_key).encode('utf-8')).digest()
        session_id = self.hashlib.sha256(hashed_rk + hashed_un).digest()
        user.session_id = session_id
        authenticator.session_id = session_id

    def hash_input(self, hash_i):
        hash_o = self.hashlib.sha256(hash_i)
        return hash_o

    def hash_salt_input(self, hash_i, salt_i):
        hash_salt_i = hash_i + salt_i
        hash_salt_o = self.hashlib.sha256(hash_salt_i.encode('utf-8'))
        return hash_salt_o.hexdigest()

    def generate_salt(self,):
        key_length = 16
        salt_bytes = self.secrets.token_bytes(key_length)
        salt = ''.join(format(byte, "02x") for byte in salt_bytes)
        return salt

    def encrypt_AES(self, plain_text, key, SQL_db):
        cipher = self.Cipher(self.algos.AES(key), self.modes.ECB(), self.default_backend())
        encryptor = cipher.encryptor()
        cipher_text = encryptor.update(plain_text) + encryptor.finalize()
        SQL_db.cipher_text = cipher_text

    def decrypt_AES(self, cipher_text, key, user):
        cipher = self.Cipher(self.algos.AES(key), self.modes.ECB(), self.default_backend())
        decryptor = cipher.decryptor()
        plain_text = decryptor.update(cipher_text) + decryptor.finalize()
        user.plain_text = plain_text
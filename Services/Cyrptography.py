# decyprt data, my implimentation of AES that will have internal hash for security
# and to verify that the implimentation is uncompromised

class Cryptography():
    class_name = "Cryptography"
    class_id = 5
    def __init__(self,
                 secret,
                 hashlib,
                 random):
        self.secret = secret
        self.hashlib = hashlib
        self.random = random

    def generate_encryption_key(self, user, salt, keylength=32, iteration=100000,):
        data = (user.username + user.password).encode('utf-8')
        self.hashlib.pbkdf2_hmac('sha256', data, salt, iteration, keylength)

    def AES(self, cypher_text, key):
        plain_text = None
        plain_text = cypher_text + key
        return plain_text
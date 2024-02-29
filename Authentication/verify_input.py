import hashlib
from user_salts import uuid
# verify input

def hash_input(hash_i):
    hash_o = hashlib.sha256(hash_i)
    return hash_o

def hash_salt_input(hash_i, salt_i):
    hash_salt_i = hash_i + salt_i
    hash_salt_o = hashlib.sha256(hash_salt_i)
    return hash_salt_o

def get_stored_hash(called_item):
    # look up in stored hash table
    stored_hash = called_item
    return stored_hash

def generate_fake_salt():
    return 0

def get_salt(username):
    for user in uuid:
        if user[0] == username:
            return user[0]
        else:
            return generate_fake_salt()

def compare_hash(called_item, generated_hash):
    stored_hash = get_stored_hash(called_item)
    if stored_hash == generated_hash:
        return True
    else:
        # log login attempt
        return False

def authenticate_logins(username, password):
    salt = get_salt(username)
    hs_attempt = hash_salt_input(password, salt)
    authentication = compare_hash(username, hs_attempt)
    return authentication
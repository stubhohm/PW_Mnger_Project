import hashlib
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

def compare_hash(called_item, generated_hash):
    stored_hash = get_stored_hash(called_item)
    if stored_hash == generated_hash:
        return True
    else:
        # log login attempt
        return False
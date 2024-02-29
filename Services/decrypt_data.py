# decyprt data, my implimentation of AES that will have internal hash for security
# and to verify that the implimentation is uncompromised

def run_AES(cypher_text, key):
    plain_text = None
    plain_text = cypher_text + key
    return plain_text
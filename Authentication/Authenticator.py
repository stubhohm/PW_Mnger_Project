# verify input
class Authenticator():
    def __init__(self, authenticated = False, session_id = None):
        self.authenticated = authenticated
        self.session_id = session_id

    def auth_logins(self, user, SQL_db):
        salt = SQL_db.get_salt(user.username)
        hs_attempt = SQL_db.hash_salt_input(user.password, salt)
        stored_hash = SQL_db.get_stored_hash(user.username)
        self.authenticated = SQL_db.compare_hash(stored_hash, hs_attempt)
        return self.authenticated
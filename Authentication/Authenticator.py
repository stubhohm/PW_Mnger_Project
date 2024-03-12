# verify input
class Authenticator():
    def __init__(self, authenticated = False, session_id = None):
        self.authenticated = authenticated
        self.session_id = session_id

    def delete_cache(self):
        self.authenticated = False
        self.session_id = None

    def auth_logins(self, user, SQL_db):
        failed_text = "Sorry, that Username or Password was incorrect"
        if not SQL_db.unique_username(user.username):
            print(failed_text)
            user.failed_attempts += 1
            return False
        salt = SQL_db.get_salt(user.username)
        hs_attempt = SQL_db.crypt.hash_salt_input(user.password, salt)
        stored_hash = SQL_db.get_stored_hash(user.username)
        self.authenticated = SQL_db.compare_hash(stored_hash, hs_attempt)
        if not self.authenticated:
            print(failed_text)
            user.failed_attempts += 1
        return self.authenticated
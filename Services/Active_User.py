# user input 
# high level implimented does not function but is a skeleton of what it needs
class ActiveUser():
    class_name = "ActiveUser"
    class_id = 3
    
    def __init__(self, 
                 hashlib,
                 session_id = None,
                 submit_state = False, 
                 username = [], 
                 password = [],
                 start_session = False,
                 active = True,
                 start_session_key = None, 
                 end_session_key = None,
                 new_user = False):
        self.session_id = session_id
        self.submit_state = submit_state
        self.username = username
        self.password = password
        self.hashlib = hashlib
        self.active = active
        self.start_session = start_session
        self.start_session_key = start_session_key
        self.end_session_key = end_session_key
        self.new_user = new_user
        

    def generate_session_id(self, random, authenticator):
        key_length = 16
        random_key = random.range(0,9)
        self.start_session = True
        for i in range(key_length):
            random_digit = random.range(0,9)
            random_key = (random_key *10) + random_digit
        hashed_un = self.hashlib.sha256(self.username)
        hashed_rk = self.hashlib.sha256(random_key)
        session_id = self.hashlib.sha256(hashed_rk + hashed_un)
        self.session_id = session_id
        authenticator.session_id = session_id

    
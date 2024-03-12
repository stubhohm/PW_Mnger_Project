# user input 
# high level implimented does not function but is a skeleton of what it needs
class ActiveUser():
    class_name = "ActiveUser"
    class_id = 3
    
    def __init__(self, 
                 hashlib,
                 session_id = None,
                 submit_state = False, 
                 username = '', 
                 password = '',
                 start_session = False,
                 active = True,
                 encryption_key = None, 
                 new_user = False,
                 plain_text = None):
        self.session_id = session_id
        self.submit_state = submit_state
        self.username = username
        self.password = password
        self.hashlib = hashlib
        self.active = active
        self.start_session = start_session
        self.encryption_key = encryption_key
        self.new_user = new_user
        self.plain_text = plain_text

    def delete_cache(self):
        self.hashlib = None
        self.session_id = None
        self.submit_state = False
        self.username = ''
        self.password = ''
        self.start_session = False
        self.active = False
        self.encryption_key = None
        self.new_user = False
        self.plain_text = None
        

    
# user input 
# high level implimented does not function but is a skeleton of what it needs
class ActiveUser():
    def __init__(self, session_id, submit_state = False, username = None, password = None):
        self.session_id = session_id
        self.submit_state = submit_state
        self.username = username
        self.password = password

    def get_key_released(self, input_system):
        a = 0

    def set_session_id(self, random, hashlib):
        key_length = 16
        random_key = random.range(0,9)
        for i in range(key_length):
            random_digit = random.range(0,9)
            random_key = (random_key *10) + random_digit
        return hashlib.sha256(random_key)
        
    def submit(self, input_system):
        key_released = self.get_key_released(input_system)
        if key_released == 0:
            self.submit_state = True
        else:
            self.submit_state = False
        return self.submit_state

    def modify_current_input(self, input_system, input):
        key_released = self.get_key_released(input_system)
        # if input is delete or backscape pop, else, append
        input.append(key_released)
        return input

    def get_user_input(self, input_system, username, password, submit_state):
        # For now if the user has submitted username and password stop gathering input
        if submit_state:
            return
        
        # If we are in the username field
        if input_system.field.value == 1:
            if self.submit(input_system):
                # If we submit the username, jump to the password field
                input_system.field.update_field(2)
                self.submit_state = False
                return
            else:
                self.username = self.modify_current_input(input_system, username)   
        
        # If we are not in username and are in the password field
        elif input_system.field.value == 2:
            if self.submit(input_system):
                # If we are in the password field submit entered credentials
                return
            else:
                self.password = self.modify_current_input(input_system, password) 


    
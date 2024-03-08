# user input 
# high level implimented does not function but is a skeleton of what it needs
class ActiveUser():
    def __init__(self, session_id, submit_state, username, password):
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
        



    def submit(self, input_system):
        key_released = self.get_key_released(input_system)
        if key_released == 0:
            return True
        else:
            return False

    def modify_current_input(self, input_system, input):
        key_released = get_key_released(input_system)
        input.append(key_released)
        return input

    def get_user_input(self, input_system, username, password, submit_state):
        if submit_state:
            return True, password, username
        if input_system.field == "username":
            if self.submit:
                input_system.field == "password"
                return False, password, username
            else:
                username = self.modify_current_input(input_system, username)
            
        if self.submit:
            return True, password, username
        password = self.modify_current_input(input_system, password)
        return False, password, username

    
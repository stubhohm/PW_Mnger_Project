class InputSystem():
    class_name = "InputSystem"
    class_id = 2
    
    def __init__(self, 
                 field,):
        self.field = field

    def get_key_released(self):
        a = 0

    def update_field(self, new_field):
        if new_field == InputFields.password.value:
            self.field = InputFields.password
        
        if new_field == InputFields.username.value:
            self.field = InputFields.username

    def submit(self, user):
        key_released = self.get_key_released()
        if key_released == 0:
            user.submit_state = True
        else:
            user.submit_state = False
        return user.submit_state

    def modify_current_input(self, input):
        key_released = self.get_key_released()
        # if input is delete or backscape pop, else, append
        input.append(key_released)
        return input

    def get_user_input(self, user):
        # For now if the user has submitted username and password stop gathering input
        if user.submit_state:
            return
        
        # If we are in the username field
        if self.field.value == 1:
            if self.submit(user):
                # If we submit the username, jump to the password field
                self.field.update_field(2)
                user.submit_state = False
                return
            else:
                user.username = self.modify_current_input(user.username)   
        
        # If we are not in username and are in the password field
        elif self.field.value == 2:
            if self.submit(user):
                # If we are in the password field submit entered credentials
                return
            else:
                self.password = self.modify_current_input(user.password) 
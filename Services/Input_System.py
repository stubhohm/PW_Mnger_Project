from ENUMS import InputFields

class InputSystem():
    def __init__(self, field):
        field = InputFields
        self.field = field

    def update_field(self, new_field):
        if new_field == InputFields.password.value:
            self.field = InputFields.password
        
        if new_field == InputFields.username.value:
            self.field = InputFields.username
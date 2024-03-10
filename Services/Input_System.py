def contain_special_character(text):
    special_characters = r"!@#$%^&*()_+={}[]:;<>,.?/\|`~\""
    return any(char in special_characters for char in text)

def unique_username(username, SQL_server):
    return True

class InputSystem():
    class_name = "InputSystem"
    class_id = 2
    
    def __init__(self, 
                 un = None,
                 pw1 = None,
                 pw2 = None,
                 active_field = False):
        self.un = un
        self.pw1 = pw1
        self.pw2 = pw2
        self.active_field = active_field

    def validate_password_complexity(self):
        pw = self.pw1.get()
        if not any(char.isdigit() for char in pw):
            return False
        if not any(char.isalpha() for char in pw):
            return False
        if not contain_special_character(pw):
            return False
        if not 7 < len(pw) < 33:
            return False
        return True
        
    def validate_username(self, SQL_server):
        un = self.un.get()
        if not 7 < len(un) < 33:
            print("Your username must be bettween 7 and 32 characters")
            return False
        if SQL_server.unique_username(un):
            print("That username is already taken")
            return False
        return True

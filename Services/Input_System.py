def contain_special_character(text):
    special_characters = r"!@#$%^&*()_+={}[]:;<>,.?/\|`~\""
    return any(char in special_characters for char in text)

def unique_username(username, SQL_server):
    return True

class InputSystem():
    class_name = "InputSystem"
    class_id = 2
    
    def __init__(self):
        
        self.un = None
        self.pw1 = None
        self.pw2 = None
        self.sub = self.SubAcct
        self.active_field = False

    class SubAcct:
        def __init__(self) -> None:
            self.un = None
            self.pw1 = None
            self.pw2 = None
            self.details = None 

    def delete_cache(self):
        self.un = None
        self.pw1 = None
        self.pw2 = None
        self.active_field = None

    def validate_password_complexity(self, min = 7, max = 33, sub_acct = False):
        if not sub_acct:
            pw = self.pw1.get()
        else:
            pw = self.sub.pw1.get()
        if not min < len(pw) < max:
            return False
        if sub_acct:
            return True
        if not any(char.isdigit() for char in pw):
            return False
        if not any(char.isalpha() for char in pw):
            return False
        if not contain_special_character(pw):
            return False
        
        return True
        
    def validate_username(self, SQL_server, min = 7, max = 33, sub_acct = False):
        if not sub_acct:
            un = self.un.get()
        else:
            un = self.sub.un.get()
        if not min < len(un) < max:
            print(f"Your username must be bettween {min + 1} and {max - 1} characters")
            return False
        if not sub_acct and SQL_server.unique_username(un):
            print("That username is already taken")
            return False
        return True

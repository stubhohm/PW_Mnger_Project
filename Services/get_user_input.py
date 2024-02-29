# user input 
# high level implimented does not function but is a skeleton of what it needs

def get_key_released(input_system):
    a = 0

def submit(input_system):
    key_released = get_key_released(input_system)
    if key_released == 0:
        return True
    else:
        return False

def modify_current_input(input_system, input):
    key_released = get_key_released(input_system)
    input.append(key_released)
    return input

def get_user_input(input_system, username, password, submit_state):
    if submit_state:
        return True, password, username
    if input_system.field == "username":
        if submit:
           input_system.field == "password"
           return False, password, username
        else:
           username = modify_current_input(input_system, username)
        
    if submit:
        return True, password, username
    password = modify_current_input(input_system, password)
    return False, password, username

    
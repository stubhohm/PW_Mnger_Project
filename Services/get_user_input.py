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

def modify_current_password(input_system, password):
    key_released = get_key_released(input_system)
    password.append(key_released)
    return password

def get_user_input(input_system, password):
    if submit:
        return True, password
    password = modify_current_password(input_system, password)
    return False, password

    
import smtplib
from Services.decrypt_data import run_AES
from Services.display_gui import update_display
from Services.get_user_input import get_user_input
from Authentication.verify_input import authenticate_logins
cypher_text_path = "\\Authentication\\salt_hash_pass.txt"
hash_table_path = "\\Authentication\\hash_table.txt"

"""
Project Goal:
To make an application that stores hashed and salted passwords in an encrypted file,
but a single login prompt from the user and second auth, if successful will allow you to 
see the applications with stored passwords that will then be decyrpted on a request 
from the user in the application
I will put in dummy passwords for random stuff like router, safe combo, bike lock etc
"""
# features
    # make honey pots for simple or rainbow table passwords that
        #log attempt data and notify the user of the attempt after a real login
    #see about some form of MFA
    #GUI 

# Things I am unsure how to handle
    # prevent email MFA spoofing via changing where it is trying to send it via code

with open(hash_table_path, "r") as hash_table:
    hash_table = hash_table.read().split()

with open(cypher_text_path, "r") as cypher_text:
    cypher_text = cypher_text.read().split()

def main():
    submit_state, username, password = get_user_input(input_system, username, password, submit_state)
    if submit_state and authenticate_logins(username, password):   
        key = get_key(username, password)
        run_AES(cypher_text, key)
    else:
        submit_state = False
    # Add/Edit/Delete password option requires a reentering password and a second MFA


if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Spline_drawer"
    )
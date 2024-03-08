import smtplib
import sqlite3
import hashlib
from Services.Cyrptography import Cyptography
from Services.GUI import GUI
from Services.Active_User import ActiveUser
from Services.SQL_Sever import SQLSever
from Services.Input_System import InputSystem
from Authentication.Authenticator import Authenticator

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

def init_instances():
    return SQLSever, ActiveUser, Authenticator, Cyptography, GUI, InputSystem

def main():
    SQL_db, user, authenticator, crypt, GUI, input_system = init_instances()
    active = True
    while active:
        user.get_user_input(input_system, user.username, user.password, submit_state)
        if user.submit_state and authenticator.auth_logins(user.username, user.password, SQL_db):   
            key = 
            crypt.AES(cypher_text, key)
        else:
            submit_state = False
        GUI.update_display(input_system)
        # Add/Edit/Delete password option requires a reentering password and a second MFA


if __name__ == "__main__":
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: Spline_drawer"
    )
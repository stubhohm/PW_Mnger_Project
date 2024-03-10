import smtplib
import sqlite3
import hashlib
import random
import secrets
from tkinter import *
from tkinter import ttk, messagebox
from Services.ENUMS import InputFields
from Services.Cyrptography import Cryptography
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
    SQLsvr = SQLSever(sqlite3, random, hashlib, secrets)
    SQLsvr.init_data_tables()
    user = ActiveUser(hashlib)
    auth = Authenticator()
    crypt = Cryptography()
    input = InputSystem()
    UI = GUI(Tk(), ttk, messagebox)
    UI.init_display()
    return SQLsvr, user, auth, crypt, UI, input 

def shutdown_procedure():
    print("shutting down")

def main():
    SQL_db, user, authenticator, crypt, GUI, input_system = init_instances()
    while user.active:
        if user.submit_state and user.new_user:
            # Submits new user data to the credentials data table
            SQL_db.add_user(user)
        if user.submit_state and authenticator.auth_logins(user, SQL_db):   
            if not user.start_session:
                # At the start of the password session generate a unique session ID
                # Generate encryption key by merging the username and salted password, then hash that merge to make the private key.
                user.start_session = True
                crypt.generate_encryption_key(user, SQL_db.get_salt(user.username))
                user.generate_session_id(random, authenticator)
            SQL_db.get_cypher_text(user.username)
            crypt.AES(SQL_db.cypher_text, user.start_session_key)
        else:
            user.submit_state = False
        GUI.update_display(user, input_system, SQL_db)
        if not user.active:
            shutdown_procedure()
        # Add/Edit/Delete password option requires a reentering password and a second MFA


if __name__ == "__main__":
    
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: pw_manager"
    )
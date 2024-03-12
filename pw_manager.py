import smtplib
import sqlite3
import hashlib
import random
import secrets
import tkinter as tk 
from tkinter import Tk, ttk, messagebox
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
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
    crypt = Cryptography(secrets, hashlib, random, Cipher, algorithms, modes, default_backend)
    SQLsvr = SQLSever(sqlite3, Cryptography(secrets, hashlib, random, Cipher, algorithms, modes, default_backend))
    SQLsvr.init_data_tables()
    user = ActiveUser(hashlib)
    auth = Authenticator()
    input = InputSystem()
    UI = GUI(Tk(), tk, ttk, messagebox)
    UI.init_display()
    return SQLsvr, user, auth, crypt, UI, input 

def update_plain_text(SQL_db, user, crypt):
    SQL_db.get_cipher_text(user.username)
    for entry in SQL_db.cipher_text:
        decrypted_entry = []
        for text in entry:
            decrpyted_text = crypt.decrypt_AES(text, user.encryption_key)
            decrypted_entry.append(decrpyted_text)
        user.plain_text.append(decrypted_entry)

def init_session(user, SQL_db, authenticator, crypt):
    if user.failed_attempts > 5:
        print("Sorry, you account is locked")
        return
    if user.start_session:
        return
    # At the start of the password session generate a unique session ID
    # Generate encryption key by merging the username and salted password, then hash that merge to make the private key.
    user.start_session = True
    user.failed_attempts = 0
    crypt.generate_encryption_key(user, SQL_db.get_salt(user.username))
    crypt.generate_session_id(user, authenticator)
    update_plain_text(SQL_db, user, crypt)
    
def continue_session(user, SQL_db, authenticator, crypt, input_system):
    if authenticator.session_id != user.session_id:
        user.active = False
        return
    if user.submit_acct:
        update_plain_text(SQL_db, user, crypt)    
    SQL_db.add_acct(user, input_system)
    
def shutdown_procedure(SQL_db,user, input, auth):
    SQL_db.close_db(user)
    user.delete_cache()
    input.delete_cache()
    auth.delete_cache()
    print("shutting down")

def main():
    SQL_db, user, authenticator, crypt, GUI, input_system = init_instances()
    SQL_db.print_all()
    while user.active:
        if user.submit_state and user.new_user:
            # Submits new user data to the credentials data table
            SQL_db.add_user(user)
        if user.submit_state and authenticator.auth_logins(user, SQL_db):   
            init_session(user, SQL_db, authenticator, crypt)
            continue_session(user, SQL_db, authenticator, crypt, input_system)
        else:
            user.submit_state = False
        GUI.update_display(user, input_system, SQL_db)
        if not user.active:
            shutdown_procedure(SQL_db, user, input_system, authenticator)
        # Add/Edit/Delete password option requires a reentering password and a second MFA

if __name__ == "__main__":
    
    main()
    print(
        "this main only runs if this file is ran, not if another program executes it: pw_manager"
    )
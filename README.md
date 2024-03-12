-- Over-Arching Premise --
The goal of this project is to make a 'secure' password manager with an API.

-- Intended Components --
Full back end project with a 'secure' manager program written in python.
Full front end with API to interact with the python programs to allow for hacking into the box.

-- Current State --
Stored login credentials are fully encrypted. Main username is stored in plaintext, along with a salt and salt and hashed password.
Data base never touches unencrpyted data, it is only stored locally on the user during a session.
At the conclusion of a session, the local user data is reencrypted into the data base saving any changes.
I am sure this will be hackable, but right now, I think this is a pretty tight ship. I will need to see if/how vunerable to injections sqlite3 is for the future.

-- Next Steps --
Add options to delete/alter credentials.
Add option to update main account password.
Make a few dummy accounts.
Improve UI appearance.


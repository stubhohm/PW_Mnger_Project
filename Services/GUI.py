def auth_un_pw(user, input_system):
    user.username = input_system.un.get()
    user.password = input_system.pw1.get()
    user.submit_state = True
    print(user.username)
    print(user.password)
    print("clicked")

def clear_window(display):
    for widget in display.winfo_children():
        widget.destroy()

def new_user(user, input_system):
    user.username = input_system.un.get()
    user.new_user = True
    input_system.active_field = False
    print(user.new_user)

def submit_new_user(user, input_system, SQL_server):
    user.username = input_system.un.get()
    pw1 = input_system.pw1.get()
    pw2 = input_system.pw2.get()
    input_system.active_field = False
    print(user.username)
    print(user.password)
    print("clicked")
    if not input_system.validate_username(SQL_server):    
        print("your password must be between 8 and 32 characters long")
        return
    if not input_system.validate_password_complexity():
        print("your password must contain a letter, number, a special character, and between 8 and 32 characters long")
        return
    if pw1 == pw2:
        user.password = pw1
        print("passwords match and is secure, making new acct")
        user.submit_state = True
        return
    else:
        print("Your passwords do not match, please try again")
        input_system.pw1.delete(0)
        input_system.pw2.delete(0)
        return
    
    
def close_window(window, user):
    if window.messagebox.askokcancel("Quit", "Do you really want to quit?"):
        user.active = False
        window.display.destroy()

def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 4
    window.geometry(f"+{x}+{y}")

class GUI():
    cass_name = "GUI"
    class_id = 4
    
    def __init__(self, display, ttk, messagebox):
        self.display = display
        self.ttk = ttk
        self.messagebox = messagebox


    def create_new_user(self, ttk, user, input_system, SQL_server):
        clear_window(self.display)
        label = ttk.Label(self.display, text='Enter your new Username')
        label.pack(pady = (15,0))
        input_system.un = ttk.Entry(self.display, width=60)
        input_system.un.pack(pady=0, padx=30)
        input_system.un.insert(0,user.username)
        label = ttk.Label(self.display, text='Enter your new Password')
        label.pack(pady = (15,0))
        input_system.pw1 = ttk.Entry(self.display, width=60)
        input_system.pw1.pack(pady=0, padx=30)
        label = ttk.Label(self.display, text='Confirm your new Password')
        label.pack(pady = (15,0))
        input_system.pw2 = ttk.Entry(self.display, width=60)
        input_system.pw2.pack(pady=0, padx=30)
        button = ttk.Button(self.display, text = "Submit", command=lambda: submit_new_user(user, input_system, SQL_server))
        button.pack(pady=20)
        input_system.active_field = True

    def input_username_password(self, ttk, user, input_system):
        clear_window(self.display)
        label = ttk.Label(self.display, text='Username')
        label.pack(pady = (15,0))
        input_system.un = ttk.Entry(self.display, width=60)
        input_system.un.pack(pady=0, padx=30)
        input_system.un.insert(0,user.username)
        label = ttk.Label(self.display, text='Password')
        label.pack(pady = (15,0))
        input_system.pw1 = ttk.Entry(self.display, width=60)
        input_system.pw1.pack(pady=0, padx=30)
        button = ttk.Button(self.display, text = "Submit", command=lambda: auth_un_pw(user, input_system))
        button.pack(pady=20)
        button = ttk.Button(self.display, text = "Create New User Account", command=lambda: new_user(user, input_system))
        button.pack(pady=20)
        input_system.active_field = True
            
    def update_display(self, user, input_system, SQL_server):
        self.display.protocol("WM_DELETE_WINDOW", lambda: close_window(self, user))
        if user.start_session and not input_system.active_field:
            a = 0
        elif not user.new_user and not input_system.active_field:
            self.input_username_password(self.ttk, user, input_system)
        elif user.new_user and not input_system.active_field:
            self.create_new_user(self.ttk, user, input_system, SQL_server)
        self.display.update()

    def init_display(self):
        center_window(self.display)
        self.display.title("Super Duper Safe Password Manager")
        

        

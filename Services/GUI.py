



class GUI():
    cass_name = "GUI"
    class_id = 4
    
    def __init__(self, display, ttk, messagebox):
        self.display = display
        self.ttk = ttk
        self.messagebox = messagebox

    def clear_window(self, display):
        for widget in display.winfo_children():
            widget.destroy()

    def new_user(self, user, input_system):
        user.username = input_system.un.get()
        user.new_user = True
        input_system.active_field = False
        print(user.new_user)

    def log_un_pw(self, user, input_system):
        user.username = input_system.un.get()
        user.password = input_system.pw1.get()
        user.submit_state = True
        print(user.username)
        print(user.password)
        print("clicked")

    def submit_new_user(self, user, input_system, SQL_server):
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
    
    def return_to_sign_in(self, user, input_system):
        user.new_user = False
        input_system.active_field = False

    def close_window(self, window, user):
        if window.messagebox.askokcancel("Quit", "Do you really want to quit?"):
            user.active = False
            window.display.destroy()

    def insert_test_names(self, input_system):
        input_system.un.insert(0, "stubhohm")
        input_system.pw1.insert(0, "dog$arec00l")
        input_system.pw2.insert(0, "dog$arec00l")
    
    def center_window(self, window):
        window.update_idletasks()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        window_width = window.winfo_width()
        window_height = window.winfo_height()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 4
        window.geometry(f"+{x}+{y}")

    def create_new_user(self, user, input_system, SQL_server):
        self.clear_window(self.display)
        label = self.ttk.Label(self.display, text='Enter your new Username')
        label.pack(pady = (15,0))
        input_system.un = self.ttk.Entry(self.display, width=60)
        input_system.un.pack(pady=0, padx=30)
        input_system.un.insert(0,user.username)
        label = self.ttk.Label(self.display, text='Enter your new Password')
        label.pack(pady = (15,0))
        input_system.pw1 = self.ttk.Entry(self.display, width=60)
        input_system.pw1.pack(pady=0, padx=30)
        label = self.ttk.Label(self.display, text='Confirm your new Password')
        label.pack(pady = (15,0))
        input_system.pw2 = self.ttk.Entry(self.display, width=60)
        input_system.pw2.pack(pady=0, padx=30)
        button_submit = self.ttk.Button(self.display, text = "Submit", command=lambda: self.submit_new_user(user, input_system, SQL_server))
        button_submit.pack(pady=20)
        button_return_to_signin = self.ttk.Button(self.display, text = "Return to Sign In", command=lambda: self.return_to_sign_in(user, input_system))
        button_return_to_signin.pack(pady=20)
        input_system.active_field = True

    def input_username_password(self, user, input_system):
        self.clear_window(self.display)
        label = self.ttk.Label(self.display, text='Username')
        label.pack(pady = (15,0))
        input_system.un = self.ttk.Entry(self.display, width=60)
        input_system.un.pack(pady=0, padx=30)
        input_system.un.insert(0,user.username)
        label = self.ttk.Label(self.display, text='Password')
        label.pack(pady = (15,0))
        input_system.pw1 = self.ttk.Entry(self.display, width=60)
        input_system.pw1.pack(pady=0, padx=30)
        button = self.ttk.Button(self.display, text = "Submit", command=lambda: self.log_un_pw(user, input_system))
        button.pack(pady=20)
        button = self.ttk.Button(self.display, text = "Create New User Account", command=lambda: self.new_user(user, input_system))
        button.pack(pady=20)
        input_system.active_field = True

    def password_menu(self, user):
        self.clear_window(self.display)
        welcome_banner = f"Welcome {user.username}!!"
        welcome_sign = self.ttk.Label(self.display, text=welcome_banner)
        welcome_sign.pack(pady = (5,20)) 

    def update_display(self, user, input_system, SQL_server):
        self.display.protocol("WM_DELETE_WINDOW", lambda: self.close_window(self, user))
        if user.start_session and not input_system.active_field:
            # Authenticated and can view stored date
            self.password_menu()
        elif not user.new_user and not input_system.active_field:
            # Main Sign in page
            self.input_username_password(user, input_system)
        elif user.new_user and not input_system.active_field:
            # Create new acct page
            self.create_new_user(user, input_system, SQL_server)
            self.insert_test_names(input_system)
        self.display.update()

    def init_display(self):
        self.center_window(self.display)
        self.display.title("Super Duper Safe Password Manager")
        

        

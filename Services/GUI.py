WIDTH = 120
HEIGHT = 100



class GUI():
    cass_name = "GUI"
    class_id = 4
    
    def __init__(self, display, tk, ttk, messagebox):
        self.display = display
        self.tk = tk
        self.ttk = ttk
        self.messagebox = messagebox
        self.show_pass = False
        self.add_acct = False

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
        input_system.active_field = False
        print(user.username)
        print(user.password)
        print("clicked")

    def submit_new_user(self, user, input_system, SQL_server, is_sub_acct):
        input_system.active_field = False
        if is_sub_acct:
            sub_un, sub_pass = (0 , 200, True), (0 , 200, True)
            pw1 = input_system.sub.pw1.get()
            pw2 = input_system.sub.pw2.get()
        else: 
            user.username = input_system.un.get()
            pw1 = input_system.pw1.get()
            pw2 = input_system.pw2.get()    
            sub_un, sub_pass = None, None
        if not input_system.validate_username(SQL_server, *sub_un if sub_un else()):    
            print("your username must be between 8 and 32 characters long")
            return
        if not input_system.validate_password_complexity(*sub_pass if sub_pass else()):
            print("your password must contain a letter, number, a special character, and between 8 and 32 characters long")
            return
        if pw1 == pw2:
            if is_sub_acct:
                print("your new account has been submitted")
                user.submit_acct = True
                self.add_acct = False
                return
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

    def return_to_acounts(self, input_system):
        self.add_acct = False
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
        input_system.active_field = True
        label_un = self.ttk.Label(self.display, text='Enter your new Username')
        label_un.pack(pady = (15,0))
        input_system.un = self.ttk.Entry(self.display, width=60)
        input_system.un.pack(pady=0, padx=30)
        input_system.un.insert(0,user.username)
        label_pw1 = self.ttk.Label(self.display, text='Enter your new Password')
        label_pw1.pack(pady = (15,0))
        input_system.pw1 = self.ttk.Entry(self.display, width=60)
        input_system.pw1.pack(pady=0, padx=30)
        label_pw2 = self.ttk.Label(self.display, text='Confirm your new Password')
        label_pw2.pack(pady = (15,0))
        input_system.pw2 = self.ttk.Entry(self.display, width=60)
        input_system.pw2.pack(pady=0, padx=30)
        button_submit = self.ttk.Button(self.display, text = "Submit", command=lambda: self.submit_new_user(user, input_system, SQL_server, False))
        button_submit.pack(pady=20)
        button_return_to_signin = self.ttk.Button(self.display, text = "Return to Sign In", command=lambda: self.return_to_sign_in(user, input_system))
        button_return_to_signin.pack(pady=20)
        
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
        input_system.pw2 = self.ttk.Entry()
        input_system.active_field = True

    def toggle_pass(self, input_system):
        if not self.show_pass:
            self.show_pass = True
        else: 
            self.show_pass = False   
        input_system.active_field = False

    def add_new_acct(self, user, input_system, SQL_server):
        self.clear_window(self.display)
        label_un = self.ttk.Label(self.display, text='Enter your accounts Username')
        label_un.pack(pady = (15,0))
        input_system.sub.un = self.ttk.Entry(self.display, width=60)
        input_system.sub.un.pack(pady=0, padx=30)
        label_pw1 = self.ttk.Label(self.display, text='Enter your accounts Password')
        label_pw1.pack(pady = (15,0))
        input_system.sub.pw1 = self.ttk.Entry(self.display, width=60)
        input_system.sub.pw1.pack(pady=0, padx=30)
        label_pw2 = self.ttk.Label(self.display, text='Confirm your accounts Password')
        label_pw2.pack(pady = (15,0))
        input_system.sub.pw2 = self.ttk.Entry(self.display, width=60)
        input_system.sub.pw2.pack(pady=0, padx=30)
        label_details = self.ttk.Label(self.display, text='Add a descrption')
        label_details.pack(pady = (15,0))
        input_system.sub.details = self.ttk.Entry(self.display, width=60)
        input_system.sub.details.pack(pady=0, padx=30)
        button_submit = self.ttk.Button(self.display, text = "Submit", command=lambda: self.submit_new_user(user, input_system, SQL_server, True))
        button_submit.pack(pady=20)
        button_submit = self.ttk.Button(self.display, text = "Return to Accounts", command=lambda: self.return_to_acounts(input_system))
        button_submit.pack(pady=20)

    def add_password(self, input_system):
        self.add_acct = True
        input_system.active_field = False

    def display_pass_table(self, user):
        table_header = f"Stored Accounts"
        table_banner = self.ttk.Label(self.display, text=table_header)
        table_banner.pack(pady = (20,5), side=self.tk.LEFT, padx = WIDTH/2)
        pass_table = self.ttk.Treeview(self.display, columns=('Column1','Column2','Column3'))
        pass_table.heading('Column1', text = 'Username')
        pass_table.heading('Column2', text = 'Password')
        pass_table.heading('Column3', text = 'Description')
        pass_table.pack(pady = (5,5), side=self.tk.LEFT)
        for row in user.plain_text:    
            data = row[-3:]
            pass_table.insert('','end',values=data)

    def password_menu(self, user, input_system, SQL_server):
        self.clear_window(self.display)
        input_system.active_field = True
        welcome_banner = f"Welcome {user.username}!!"
        welcome_sign = self.ttk.Label(self.display, text=welcome_banner)
        welcome_sign.pack(pady = (5,20), padx = WIDTH * 2)
        if self.add_acct:
            self.add_new_acct(user, input_system, SQL_server)
            return
        button_text= ''
        if not self.show_pass:
            button_text = 'Show Accounts and Passwords'
        else:
            button_text = 'Hide Accounts and Passwords'
            SQL_server.get_cipher_text(user.username)

        toggle_pass = self.ttk.Button(self.display, text = button_text, command=lambda: self.toggle_pass(input_system))
        toggle_pass.pack(pady=20, side=self.tk.LEFT, padx=(WIDTH/2, 0))

        add_pass = self.ttk.Button(self.display, text = 'Add Account', command=lambda: self.add_password(input_system))
        add_pass.pack(pady=20, side=self.tk.RIGHT, padx=(0, WIDTH/2))
        if self.show_pass:
            self.display_pass_table(user)
        else:
            print("we are hiding stuff")

    def update_display(self, user, input_system, SQL_server):
        self.display.protocol("WM_DELETE_WINDOW", lambda: self.close_window(self, user))
        if user.start_session and not input_system.active_field:
            # Authenticated and can view stored date
            self.password_menu(user, input_system, SQL_server)
        elif not user.new_user and not input_system.active_field:
            # Main Sign in page
            self.input_username_password(user, input_system)
            self.insert_test_names(input_system,)
        elif user.new_user and not input_system.active_field:
            # Create new acct page
            self.create_new_user(user, input_system, SQL_server)    
            #self.insert_test_names(input_system)
        self.display.update()

    def init_display(self):
        self.center_window(self.display)
        self.display.title("Super Duper Safe Password Manager")
        

        

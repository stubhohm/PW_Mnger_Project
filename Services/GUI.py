def on_click(user, input_system):
    user.username = input_system.un
    user.password = input_system.pw
    print(user.username)
    print(user.password)
    print("clicked")


class GUI():
    cass_name = "GUI"
    class_id = 4
    
    def __init__(self, display):
        self.display = display


    def update_display(self, ttk, user, input_system):
        button = ttk.Button(self.display, text = "Submit", command=lambda: on_click(user, input_system))
        button.pack(pady=20)
        self.display.mainloop()
    
    def init_dispaly(self, ttk, input_system):
        self.display.title("Super Duper Safe Password Manager")
        label = ttk.Label(self.display, text='Username')
        label.pack(pady = (15,0))
        input_system.un = ttk.Entry(self.display, width=60)
        input_system.un.pack(pady=0, padx=30)
        label = ttk.Label(self.display, text='Password')
        label.pack(pady = (15,0))
        input_system.pw = ttk.Entry(self.display, width=60)
        input_system.pw.pack(pady=0, padx=30)

        

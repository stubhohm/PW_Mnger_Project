def on_click():
    print("clicked")


class GUI():
    cass_name = "GUI"
    class_id = 4
    
    def __init__(self, display):
        self.display = display


    def update_display(self,user):
        self.display.mainloop()
    
    def init_dispaly(self, ttk):
        self.display.title("Super Duper Safe Password Manager")
        label = ttk.Label(self.display, text='Username')
        label.pack(pady = 15)
        un_input = ttk.Entry(self.display, width=60)
        un_input.pack(pady=0, padx=30)
        label = ttk.Label(self.display, text='Password')
        label.pack(pady = 15)
        pw_input = ttk.Entry(self.display, width=60)
        pw_input.pack(pady=0, padx=30)    
        button = ttk.Button(self.display, text = "Submit", command=on_click())
        button.pack(pady=20)

        

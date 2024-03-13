import tkinter as tk
import customtkinter
from Blinder import Blinder
from icecream import ic

class App(customtkinter.CTk):
    
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    
    def __init__ (self):
        super().__init__()
        
        self.geometry("640x480")
        self.minsize(width=320, height=240)
        self.title('Blinder')
        
        # self.menu = Menu(self)
        self.title_ = customtkinter.CTkLabel(master=self, text="Blinder", font=("Nunito", 40))
        self.title_.pack(anchor='center')
        self.body = Window(self)
        
        self.mainloop()
# END CLASS

# Body class
class Window(customtkinter.CTkFrame):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.set_grid()
        self.parent = parent
        
        self.browse_label = customtkinter.CTkLabel(master=self, text="Browse your files", text_color='gray', width=400)
        self.browse_label.grid(row=0, column=0, columnspan=2, sticky='ew')
        self.paths = []
        self.browse_button = customtkinter.CTkButton(master=self, text="Browse files", command=self.browse_file)
        self.browse_button.grid(row=1, column=0, sticky='ew')
        self.crypt_button = customtkinter.CTkButton(master=self, text="Encrypt / Decrypt", command=self.translate)
        self.crypt_button.grid(row=1, column=1, sticky='ew')
        self.message_label = customtkinter.CTkLabel(master=self, text='', font=("Nunit", 16, "bold"))
        self.message_label.grid(row=2, column=0, columnspan=2)
        
        self.pack()
    # END FUNCTION
    
    # use as command to browse files     
    def browse_file(self):
        self.selected_data = customtkinter.filedialog.askopenfiles(title="Select files")
        
        for file in self.selected_data:
            self.paths.append(file.name)
        self.browse_label.configure(text=self.paths)
        self.selected_data = None
    # END FUNCTION
    
    def translate(self):
        blinder = Blinder()
        self.browse_label.configure(text="")
        
        for file in self.paths:
            if '_bl' in file:
                blinder.clarify(file)
            else:
                blinder.obfuscate(file)

        self.paths = []
        self.message_label.configure(text="Operation done !")
    # END FUNCTION
    
    # set grid layout for window main frame
    def set_grid(self):
        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=1)
        self.rowconfigure(index=2, weight=1)
        
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)
    # END FUNCTION
    
# END CLASS

class Menu(tk.Menu):
    
    def __init__(self, parent):
        super().__init__(parent, bg='#333333', fg='white', activebackground="#666666", activeforeground="white")
        
        self.file_menu = tk.Menu(self, tearoff=0, bg='#333333', fg='white', activebackground="#666666", activeforeground="white")
        self.file_menu.add_command(label="Option 1", command=self.option1_callback)
        self.file_menu.add_command(label="Option 2", command=self.option2_callback)
        self.file_menu.add_command(label="Option 3", command=self.option3_callback)
        self.add_cascade(label="Fichier", menu=self.file_menu, activebackground="#666666", activeforeground="white")
        
        parent.config(menu=self)
        
    # END FUNCTION
    
    def option1_callback(self):
        print("option 1 selected")
    # END FUNCTION
    
    def option2_callback(self):
        print("option 1 selected")
    # END FUNCTION
    
    def option3_callback(self):
        print("option 1 selected")
    # END FUNCTION
    
# END FUCNTION

app = App()
import customtkinter as ctk
from settings import *
from home import *
from PIL import Image
import os
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass


class App(ctk.CTk):
    width = 900
    height = 600
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("CustomTkinter example_background_image.py")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        # load and create background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        print(current_path)
        self.bg_image = ctk.CTkImage(Image.open(current_path + "/bg_gradient.jpg"),
                                               size=(self.width, self.height))
        self.bg_image_label = ctk.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        # create login frame
        self.login_frame = ctk.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")
        self.login_label = ctk.CTkLabel(self.login_frame, text="Login Page",
                                                  font=ctk.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.username_entry = ctk.CTkEntry(self.login_frame, width=200, placeholder_text="username")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.password_entry = ctk.CTkEntry(self.login_frame, width=200, show="*", placeholder_text="password")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
        self.login_button = ctk.CTkButton(self.login_frame, text="Login", command=self.clique, width=200)
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))

        
        self.mainloop()
        
    def change_title_bar_color(self):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR = TITLE_HEX_COLOR
            windll.dwmapi.DwmSetWindowAttribute(HWND,DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
        except:
            print('ola')
        
    def clique(self):
        if self.username_entry.get() == 'erikp':
            Home(self)
            self.withdraw()
            
    
        
if __name__ =='__main__':
    App()
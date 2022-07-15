import tkinter
import customtkinter
from matplotlib.pyplot import fill

class mainFrame(customtkinter.CTk):
    WIDTH = 1024
    HEIGHT = 600
    def __init__(self):
        customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

        super().__init__()

        self.title("Microtunel control")
        self.geometry(f"{mainFrame.WIDTH}x{mainFrame.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed
        #self.overrideredirect(1)
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=10)
        self.frame_left.grid(row=0, column=0, sticky="ns",pady=10,padx=10)

        # ============ create left and windows frames  ============
        # The menu is on the left
        # Windows are on the right
# configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(6,weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Menú",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Inicio",
                                                command=self.button_start)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Control",
                                                command=self.button_control)
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Historico",
                                                command=self.button_historico)
        self.button_3.grid(row=4, column=0, pady=10, padx=20)

        self.button_4 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Usuarios",
                                                command=self.button_user)
        self.button_4.grid(row=5, column=0, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Apariencia")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Dark","Light" , "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

#Acà está 
    def show_frame(self,window):
        self.current_window = window
        self.current_window.frame.grid(row=0, column=1, pady=10, padx=10)

    def hide_frame(self):
        self.current_window.frame.destroy()

    def on_closing(self, event=0):
        self.destroy()

    def button_start(self):
        print("general")
    
    def button_control(self):
        print("control")

    def button_historico(self):
        print("historico")

    def button_user(self):
        print("usuarios")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

   
if __name__ == "__main__":
    app = mainFrame()
    app.mainloop()
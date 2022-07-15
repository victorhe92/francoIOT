import tkinter
import customtkinter
from matplotlib.pyplot import grid
from mainFrame import mainFrame

class control():
    
    def __init__(self,master):

        ######### GENERAL FRAME #########
        self.frame = customtkinter.CTkFrame(master=master)
        self.frame.columnconfigure((0,1,2,3),weight=1)

        self.frame.grid(row=0, column=1,sticky="nsew",pady=10,padx=10)

        ######## TITLE ############
        self.label_usuarios = customtkinter.CTkLabel(master=self.frame,   
                                                        text="Usuarios",
                                                        text_font=("Roboto Medium", -20))
                       
        self.label_usuarios.grid(row = 0,column = 0, sticky="",columnspan=4,pady=10)

       
         #####Create and delete users#######
        self.button_create_user = customtkinter.CTkButton(master=self.frame,
                                                    text="Crear usuario",
                                                    command=self.create_user)
        self.button_create_user.grid(row=3, column=2, columnspan=2, pady=25)

        self.entry_user = customtkinter.CTkEntry(master=self.frame,
                                                    placeholder_text="Usuario")
        
        self.entry_user.grid(row=3, column=0,rowspan=2)

        self.entry_pass = customtkinter.CTkEntry(master=self.frame,
                                                placeholder_text="Password",
                                                show="*")

        self.entry_pass.grid(row=3,column=1,rowspan=2)

        self.button_delete_user = customtkinter.CTkButton(master=self.frame,
                                                    text="Eliminar usuario",
                                                    command=self.delete_user)
        self.button_delete_user.grid(row=4, column=2, columnspan=2)


        ##### Label estados #####

        self.label_state = customtkinter.CTkLabel(master=self.frame,
                                                 text = "Ingrese un usuario y password")
        
        self.label_state.grid(row=5,columnspan=4,pady=25)

   

    def create_user(self):
        pass
            

    def delete_user(self):
        pass
        
if __name__=="__main__":
    app = mainFrame()
    windows_start = control(app)
    app.show_frame(windows_start)
    #app.hide_frame()
    app.mainloop()
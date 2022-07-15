import tkinter
import customtkinter
from matplotlib.pyplot import grid
from mainFrame import mainFrame

class control():
   
    def __init__(self,master):

        ######### GENERAL FRAME #########
        self.frame = customtkinter.CTkFrame(master=master)
        self.frame.columnconfigure((0,1),weight=1)

        self.frame.grid(row=0, column=1,sticky="nsew",pady=10,padx=10)

        ######## TITLE ############
        self.label_title = customtkinter.CTkLabel(master=self.frame,   
                                                        text="Registro de lotes",
                                                        text_font=("Roboto Medium", -20))
                       
        self.label_title.grid(row = 0,column = 0,pady=25,columnspan=2)

       
         ##### Datos para registro de lotes #######

        self.label_nombre = customtkinter.CTkLabel(master=self.frame,
                                                        text="Nombre de lote: ",
                                                        text_font=("Roboto Medium", -15))
        self.label_nombre.grid(row=1,column=0,columnspan=2)

        self.entry_name = customtkinter.CTkEntry(master=self.frame,
                                                placeholder_text="Nombre de lote")
        self.entry_name.grid(row=2,column=0,columnspan=2,pady=25,)

        self.label_description = customtkinter.CTkLabel(master=self.frame,
                                                        text="Descripción del lote: ",
                                                        text_font=("Roboto Medium", -15))
        self.label_description.grid(row=3,column=0,columnspan=2)

        self.entry_description = tkinter.Text(master=self.frame,height=10,width=30)
        self.entry_description.grid(row=4,column=0,columnspan=2,pady=25)

        self.button_create = customtkinter.CTkButton(master=self.frame,
                                                    text="Crear registro",
                                                    command=self.create_register)

        self.button_create.grid(row=5,column=0,columnspan=2)

    def create_register(self):
        pass
            
        
if __name__=="__main__":
    app = mainFrame()
    windows_start = control(app)
    app.show_frame(windows_start)
    #app.hide_frame()
    app.mainloop()
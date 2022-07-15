
import tkinter
import customtkinter
import datetime


class mainFrame(customtkinter.CTk):
    WIDTH = 1024
    HEIGHT = 600
    t1 = 10
    t2 = 20
    t3 = 30
    t4 = 40
    tiempo = datetime.datetime.now()
    irrigation_state = "ON"
    ventilation_state = "OFF"
    __button_irrigation_text = "Desactivar"
    __button_ventilation_text = "ON"
    def __init__(self):
        customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

        super().__init__()

        self.title("Microtunel control")
        self.geometry(f"{mainFrame.WIDTH}x{mainFrame.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed
        #self.overrideredirect(1)
        self.create_menu()
        self.create_control()
        self.create_users()
        self.create_start()
        
    def create_menu(self):
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


    def create_start(self):
        self.frame_inicio = customtkinter.CTkFrame(master=self)

        self.frame_inicio.grid(row=0, column=1,sticky="nsew",pady=10,padx=10)
        
        # ============ frame_inicio_sensors ============
        
        # configure grid layout (3x2)
        
        self.frame_inicio.columnconfigure(0,weight=1)
        self.frame_inicio.columnconfigure(1,weight=1)
        self.frame_inicio.rowconfigure(0,weight=1)
        self.frame_inicio.rowconfigure(1,weight=1)
        self.frame_inicio.rowconfigure(2,weight=1)
        
        self.label_1 = customtkinter.CTkLabel(master=self.frame_inicio,
                                              text="Control de microtuneles",
                                              text_font=("Roboto Medium", -25))  # font name and size in px
        self.label_1.grid(row=0, column=0, pady=10, padx=10, columnspan=2)
        self.label_1 = customtkinter.CTkLabel(master=self.frame_inicio,
                                              text=self.tiempo,
                                              text_font=("Roboto Medium", -12))  # font name and size in px
        self.label_1.grid(row=0, column=0, pady=10, padx=10, columnspan=2,sticky="e")

        self.frame_station1 = customtkinter.CTkFrame(master=self.frame_inicio)
        #self.frame_station1.grid_propagate(0)
        self.frame_station1.grid(row=1, column=0,pady=20, padx=20, sticky="nsew")

        self.frame_station2 = customtkinter.CTkFrame(master=self.frame_inicio)
        self.frame_station2.grid(row=1, column=1, pady=20, padx=20, sticky="nsew")

        self.frame_station3 = customtkinter.CTkFrame(master=self.frame_inicio)
        self.frame_station3.grid(row=2, column=0, pady=20, padx=20, sticky="nsew")

        self.frame_station4 = customtkinter.CTkFrame(master=self.frame_inicio)
        self.frame_station4.grid(row=2, column=1, pady=20, padx=20, sticky="nsew")

        #==============INFORMATION OF EACH STATION======================

        #===STATION 1=====
        self.frame_station1.columnconfigure(1,weight=2)
        self.frame_station1.rowconfigure(2,weight=1)

        self.lbl_station1_title = customtkinter.CTkLabel(master=self.frame_station1,
                                              text="Microtunel 1",
                                              text_font=("Roboto Medium", -20))  # font name and size in px
        self.lbl_station1_title.grid(row=0,column=0,columnspan=2,pady=10)

        self.lbl_station1_temperature_txt = customtkinter.CTkLabel(master=self.frame_station1,
                                              text="Temperatura:",
                                              text_font=("Roboto Medium", -15))  # font name and size in px
        self.lbl_station1_temperature_txt.grid(row=1,column=0,padx=10,sticky="n")

        self.lbl_station1_humidity_txt = customtkinter.CTkLabel(master=self.frame_station1,
                                              text="Humedad:",
                                              text_font=("Roboto Medium", -15))  # font name and size in px
        self.lbl_station1_humidity_txt.grid(row=1,column=1,padx=10,sticky="n")

        self.lbl_station1_temperature = customtkinter.CTkLabel(master=self.frame_station1,
                                              text=str(self.t1)+"ºC",
                                              text_font=("Roboto Medium", -56))  # font name and size in px
        self.lbl_station1_temperature.grid(row=2,column=0,padx=10,sticky="n")

        self.lbl_station1_humidity = customtkinter.CTkLabel(master=self.frame_station1,
                                              text="55%",
                                              text_font=("Roboto Medium", -56))  # font name and size in px
        self.lbl_station1_humidity.grid(row=2,column=1,padx=10,sticky="n")

        self.button_station1 = customtkinter.CTkButton(master=self.frame_station1,
                                                text="Detalles",
                                                command=self.button_event)
        self.button_station1.grid(row=3, column=0, pady=10, padx=20, columnspan=2)
  



         #===STATION 2=====
        self.frame_station2.columnconfigure(1,weight=1)
        self.frame_station2.rowconfigure(3,weight=1)

        self.lbl_station2_title = customtkinter.CTkLabel(master=self.frame_station2,
                                              text="Microtunel 2",
                                              text_font=("Roboto Medium", -20))  # font name and size in px
        self.lbl_station2_title.grid(row=0,column=0,columnspan=2,pady=10)

        self.lbl_station2_temperature_txt = customtkinter.CTkLabel(master=self.frame_station2,
                                              text="Temperatura:",
                                              text_font=("Roboto Medium", -15))  # font name and size in px
        self.lbl_station2_temperature_txt.grid(row=1,column=0,padx=10,sticky="n")

        self.lbl_station2_humidity_txt = customtkinter.CTkLabel(master=self.frame_station2,
                                              text="Humedad:",
                                              text_font=("Roboto Medium", -15))  # font name and size in px
        self.lbl_station2_humidity_txt.grid(row=1,column=1,padx=10,sticky="n")

        self.lbl_station2_temperature = customtkinter.CTkLabel(master=self.frame_station2,
                                              text=str(self.t2)+"ºC",
                                              text_font=("Roboto Medium", -56))  # font name and size in px
        self.lbl_station2_temperature.grid(row=2,column=0,padx=10,sticky="n")

        self.lbl_station2_humidity = customtkinter.CTkLabel(master=self.frame_station2,
                                              text="35%",
                                              text_font=("Roboto Medium", -56))  # font name and size in px
        self.lbl_station2_humidity.grid(row=2,column=1,padx=10,sticky="n")

        self.button_station2 = customtkinter.CTkButton(master=self.frame_station2,
                                                text="Detalles",
                                                command=self.button_event)
        self.button_station2.grid(row=3, column=0, pady=10, padx=20, columnspan=2)

        #===STATION 3=====
        self.frame_station3.columnconfigure(1,weight=1)
        self.frame_station3.rowconfigure(3,weight=1)

        self.lbl_station3_title = customtkinter.CTkLabel(master=self.frame_station3,
                                              text="Microtunel 3",
                                              text_font=("Roboto Medium", -20))  # font name and size in px
        self.lbl_station3_title.grid(row=0,column=0,columnspan=2,pady=10)

        self.lbl_station3_temperature_txt = customtkinter.CTkLabel(master=self.frame_station3,
                                              text="Temperatura:",
                                              text_font=("Roboto Medium", -15))  # font name and size in px
        self.lbl_station3_temperature_txt.grid(row=1,column=0,padx=10,sticky="n")

        self.lbl_station3_humidity_txt = customtkinter.CTkLabel(master=self.frame_station3,
                                              text="Humedad:",
                                              text_font=("Roboto Medium", -15))  # font name and size in px
        self.lbl_station3_humidity_txt.grid(row=1,column=1,padx=10,sticky="n")

        self.lbl_station3_temperature = customtkinter.CTkLabel(master=self.frame_station3,
                                              text=str(self.t3)+"ºC",
                                              text_font=("Roboto Medium", -56))  # font name and size in px
        self.lbl_station3_temperature.grid(row=2,column=0,padx=10,sticky="n")

        self.lbl_station3_humidity = customtkinter.CTkLabel(master=self.frame_station3,
                                              text="35%",
                                              text_font=("Roboto Medium", -56))  # font name and size in px
        self.lbl_station3_humidity.grid(row=2,column=1,padx=10,sticky="n")

        self.button_station3 = customtkinter.CTkButton(master=self.frame_station3,
                                                text="Detalles",
                                                command=self.button_event)
        self.button_station3.grid(row=3, column=0, pady=10, padx=20, columnspan=2)

        #===STATION 4=====
        self.frame_station4.columnconfigure(1,weight=1)
        self.frame_station4.rowconfigure(3,weight=1)

        self.lbl_station4_title = customtkinter.CTkLabel(master=self.frame_station4,
                                              text="Microtunel 4",
                                              text_font=("Roboto Medium", -20))  # font name and size in px
        self.lbl_station4_title.grid(row=0,column=0,columnspan=2,pady=10)

        self.lbl_station4_temperature_txt = customtkinter.CTkLabel(master=self.frame_station4,
                                              text="Temperatura:",
                                              text_font=("Roboto Medium", -15))  # font name and size in px
        self.lbl_station4_temperature_txt.grid(row=1,column=0,padx=10,sticky="n")

        self.lbl_station4_humidity_txt = customtkinter.CTkLabel(master=self.frame_station4,
                                              text="Humedad:",
                                              text_font=("Roboto Medium", -15))  # font name and size in px
        self.lbl_station4_humidity_txt.grid(row=1,column=1,padx=10,sticky="n")

        self.lbl_station4_temperature = customtkinter.CTkLabel(master=self.frame_station4,
                                              text=str(self.t4)+"ºC",
                                              text_font=("Roboto Medium", -56))  # font name and size in px
        self.lbl_station4_temperature.grid(row=2,column=0,padx=10,sticky="n")

        self.lbl_station4_humidity = customtkinter.CTkLabel(master=self.frame_station4,
                                              text="35%",
                                              text_font=("Roboto Medium", -56))  # font name and size in px
        self.lbl_station4_humidity.grid(row=2,column=1,padx=10,sticky="n")

        self.button_station4 = customtkinter.CTkButton(master=self.frame_station4,
                                                text="Detalles",
                                                command=self.button_event)
        self.button_station4.grid(row=3, column=0, pady=10, padx=20, columnspan=2)

    def create_control(self):
        ######### GENERAL FRAME #########
        self.frame_control = customtkinter.CTkFrame(master=self)
        self.frame_control.columnconfigure((0,1,2,3),weight=1)

        self.frame_control.grid(row=0, column=1,sticky="nsew",pady=10,padx=10)

        ######## TITLE ############
        self.label_control = customtkinter.CTkLabel(master=self.frame_control,   
                                                        text="Control",
                                                        text_font=("Roboto Medium", -20))
                       
        self.label_control.grid(row = 0,column = 0, sticky="",columnspan=4,pady=10)

        ###### Each title #####

        self.label_irrigation_title = customtkinter.CTkLabel(master=self.frame_control,   
                                                        text="Estado riego:",
                                                        text_font=("Roboto Medium", -20))
                       
        self.label_irrigation_title.grid(row = 1,column = 0, sticky="",columnspan=2)


        self.label_ventilation_title = customtkinter.CTkLabel(master=self.frame_control,   
                                                        text="Estado riego:",
                                                        text_font=("Roboto Medium", -20))
                       
        self.label_ventilation_title.grid(row = 1,column = 2, sticky="",columnspan=2)

        ##### States #####

        self.label_irrigation = customtkinter.CTkLabel(master=self.frame_control,   
                                                        text=self.irrigation_state,
                                                        text_font=("Roboto Medium", -70))
        
        self.label_irrigation.grid(row = 2,column = 0, columnspan=2)

        self.label_ventilation = customtkinter.CTkLabel(master=self.frame_control,   
                                                        text=self.ventilation_state,
                                                        text_font=("Roboto Medium", -70))
        
        self.label_ventilation.grid(row = 2,column = 2, columnspan=2)

        ##### Button states #######
        self.button_irrigation_change = customtkinter.CTkButton(master=self.frame_control,
                                                    text=self.__button_irrigation_text,
                                                    command=self.irrigation_change)
        self.button_irrigation_change.grid(row=3, column=0, columnspan=2)


        self.button_ventilation_change = customtkinter.CTkButton(master=self.frame_control,
                                                    text=self.__button_ventilation_text,
                                                    command=self.ventilation_change)
        self.button_ventilation_change.grid(row=3, column=2, columnspan=2)

         ######## TITLE 2############
        self.label_itinerario = customtkinter.CTkLabel(master=self.frame_control,   
                                                        text="Itinerario",
                                                        text_font=("Roboto Medium", -20))
                       
        self.label_itinerario.grid(row = 4,column = 0, sticky="",columnspan=4,pady=10)


        ####### Itineary irrigation label #########
        self.label_itinerario_irrigation = customtkinter.CTkLabel(master=self.frame_control,   
                                                        text="Riego\nhora inicio / hora fin ",
                                                        text_font=("Roboto Medium", -15))
                       
        self.label_itinerario_irrigation.grid(row = 5,column = 0, sticky="",columnspan=2,pady=10)

        self.label_itinerario_ventilation = customtkinter.CTkLabel(master=self.frame_control,   
                                                        text="Ventilación\nhora inicio / hora fin ",
                                                        text_font=("Roboto Medium", -15))
                       
        self.label_itinerario_ventilation.grid(row = 5,column = 2, sticky="",columnspan=2,pady=10)


        ### Itinerary listbox irrigation  ####
        self.list_irrigation_itinerary = tkinter.Listbox(master=self.frame_control,
                                                        width=30,
                                                        font=("Roboto Medium", -15),
                                                        bg="white")


        self.list_irrigation_itinerary.insert(1, "1) 15:00/15:10")
        self.list_irrigation_itinerary.insert(2, "2) 15:00/15:10")
        self.list_irrigation_itinerary.insert(3, "3) 15:00/15:10")
        self.list_irrigation_itinerary.insert(4, "4) 15:00/15:10")
        self.list_irrigation_itinerary.insert(5, "5) 15:00/15:10")
        self.list_irrigation_itinerary.insert(6, "6) 15:00/15:10")
        self.list_irrigation_itinerary.insert(7, "7) 15:00/15:10")
        self.list_irrigation_itinerary.insert(8, "8) 15:00/15:10")
        self.list_irrigation_itinerary.insert(9, "9) 15:00/15:10")
        self.list_irrigation_itinerary.insert(10, "10) 15:00/15:10")
        self.list_irrigation_itinerary.insert(11, "11) 15:00/15:10")
        self.list_irrigation_itinerary.insert(12, "12) 15:00/15:10")

        self.list_irrigation_itinerary.grid(row=6,column=0,columnspan=2)

        self.list_ventilation_itinerary = tkinter.Listbox(master=self.frame_control,
                                                        width=30,
                                                        font=("Roboto Medium", -15),
                                                        bg="white")

        self.list_ventilation_itinerary.insert(1, "1) 15:00/15:10")
        self.list_ventilation_itinerary.insert(2, "2) 15:00/15:10")
        self.list_ventilation_itinerary.insert(3, "3) 15:00/15:10")
        self.list_ventilation_itinerary.insert(4, "4) 15:00/15:10")
        self.list_ventilation_itinerary.insert(5, "5) 15:00/15:10")
        self.list_ventilation_itinerary.insert(6, "6) 15:00/15:10")
        self.list_ventilation_itinerary.insert(7, "7) 15:00/15:10")
        self.list_ventilation_itinerary.insert(8, "8) 15:00/15:10")
        self.list_ventilation_itinerary.insert(9, "9) 15:00/15:10")
        self.list_ventilation_itinerary.insert(10, "10) 15:00/15:10")
        self.list_ventilation_itinerary.insert(11, "11) 15:00/15:10")
        self.list_ventilation_itinerary.insert(12, "12) 15:00/15:10")

        self.list_ventilation_itinerary.grid(row=6,column=2,columnspan=2)

        self.frame_label_irrigation = customtkinter.CTkFrame(master=self.frame_control,
                                                            corner_radius=20)

        self.frame_label_irrigation.columnconfigure((0,1,2,3,4,5,6),weight=1)

        self.frame_label_irrigation.grid(row=7,column=0,columnspan=2,pady=10,padx=10)

        self.label_encendido_hora = customtkinter.CTkLabel(master=self.frame_label_irrigation,
                                                text="Hora encendido")
        self.label_encendido_hora.grid(row=0,column=0,columnspan=3,sticky="")

        self.spinbox_irrigation_hour = tkinter.Spinbox(master=self.frame_label_irrigation,
                                                        width=3)
        self.spinbox_irrigation_hour.grid(row=1,column=0,pady=10,padx=10,sticky="w")

        self.label_dos_puntos = customtkinter.CTkLabel(master=self.frame_label_irrigation,
                                                text=":")
        self.label_dos_puntos.grid(row=1,column=1)

        

        self.spinbox_irrigation_minute = tkinter.Spinbox(master=self.frame_label_irrigation,
                                                        width=3)
        self.spinbox_irrigation_minute.grid(row=1,column=2,pady=10,padx=10)

        self.label_hora_apagado = customtkinter.CTkLabel(master=self.frame_label_irrigation,
                                                text="Hora apagado")
        self.label_hora_apagado.grid(row=0,column=3,columnspan=3)


    def create_users(self):
        ######### GENERAL FRAME #########
        self.frame_users = customtkinter.CTkFrame(master=self)
        self.frame_users.columnconfigure((0,1,2,3),weight=1)

        self.frame_users.grid(row=0, column=1,sticky="nsew",pady=10,padx=10)

        ######## TITLE ############
        self.label_usuarios = customtkinter.CTkLabel(master=self.frame_users,   
                                                        text="Usuarios",
                                                        text_font=("Roboto Medium", -20))
                       
        self.label_usuarios.grid(row = 0,column = 0, sticky="",columnspan=4,pady=10)

       
         #####Create and delete users#######
        self.button_create_user = customtkinter.CTkButton(master=self.frame_users,
                                                    text="Crear usuario",
                                                    command=self.create_user)
        self.button_create_user.grid(row=3, column=2, columnspan=2, pady=25)

        self.entry_user = customtkinter.CTkEntry(master=self.frame_users,
                                                    placeholder_text="Usuario")
        
        self.entry_user.grid(row=3, column=0,rowspan=2)

        self.entry_pass = customtkinter.CTkEntry(master=self.frame_users,
                                                placeholder_text="Password",
                                                show="*")

        self.entry_pass.grid(row=3,column=1,rowspan=2)

        self.button_delete_user = customtkinter.CTkButton(master=self.frame_users,
                                                    text="Eliminar usuario",
                                                    command=self.delete_user)
        self.button_delete_user.grid(row=4, column=2, columnspan=2)


        ##### Label estados #####

        self.label_state = customtkinter.CTkLabel(master=self.frame_users,
                                                 text = "Ingrese un usuario y password")
        
        self.label_state.grid(row=5,columnspan=4,pady=25)

    def button_event(self):
        print("detalles")

    def show_frame(self,window):
        #self.current_window = window
        #self.current_window.frame.grid(row=0, column=1, pady=10, padx=10)
        pass
    
    def hide_frame(self):
        self.current_window.frame.destroy()

    def on_closing(self, event=0):
        self.destroy()

    def button_start(self):
        print("Inicio")
        self.frame_inicio.grid()
        self.frame_control.grid_remove()
        self.frame_users.grid_remove()
    
    def button_control(self):
        print("control")
        self.frame_control.grid()
        self.frame_inicio.grid_remove()
        self.frame_users.grid_remove()
        

    def button_historico(self):
        print("historico")

    def button_user(self):
        print("usuarios")
        self.frame_users.grid()
        self.frame_inicio.grid_remove()
        self.frame_control.grid_remove()

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
    def button_send(self):
        print(self.start_text.get())

    def update(self):
        self.label_irrigation['text']=(self.irrigation_state)
        self.button_irrigation_change.set_text(self.__button_irrigation_text)

    def irrigation_change(self):
        if(self.irrigation_state == "ON"):
            self.irrigation_state = "OFF"
            self.__button_irrigation_text = "Activar"
        else:
            self.irrigation_state = "ON"
            self.__button_irrigation_text = "Desactivar"
        self.update()
            

    def ventilation_change(self):
        pass
    
    def create_user(self):
        pass
            

    def delete_user(self):
        pass

   
if __name__ == "__main__":
    app = mainFrame()
    app.mainloop()
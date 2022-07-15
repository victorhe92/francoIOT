import tkinter
import customtkinter
from matplotlib.pyplot import grid
from mainFrame import mainFrame

class control():
    irrigation_state = "ON"
    ventilation_state = "OFF"
    __button_irrigation_text = "Desactivar"
    __button_ventilation_text = "ON"
    def __init__(self,master):

        ######### GENERAL FRAME #########
        self.frame = customtkinter.CTkFrame(master=master)
        self.frame.columnconfigure((0,1,2,3),weight=1)

        self.frame.grid(row=0, column=1,sticky="nsew",pady=10,padx=10)

        ######## TITLE ############
        self.label_control = customtkinter.CTkLabel(master=self.frame,   
                                                        text="Control",
                                                        text_font=("Roboto Medium", -20))
                       
        self.label_control.grid(row = 0,column = 0, sticky="",columnspan=4,pady=10)

        ###### Each title #####

        self.label_irrigation_title = customtkinter.CTkLabel(master=self.frame,   
                                                        text="Estado riego:",
                                                        text_font=("Roboto Medium", -20))
                       
        self.label_irrigation_title.grid(row = 1,column = 0, sticky="",columnspan=2)


        self.label_ventilation_title = customtkinter.CTkLabel(master=self.frame,   
                                                        text="Estado riego:",
                                                        text_font=("Roboto Medium", -20))
                       
        self.label_ventilation_title.grid(row = 1,column = 2, sticky="",columnspan=2)

        ##### States #####

        self.label_irrigation = customtkinter.CTkLabel(master=self.frame,   
                                                        text=self.irrigation_state,
                                                        text_font=("Roboto Medium", -70))
        
        self.label_irrigation.grid(row = 2,column = 0, columnspan=2)

        self.label_ventilation = customtkinter.CTkLabel(master=self.frame,   
                                                        text=self.ventilation_state,
                                                        text_font=("Roboto Medium", -70))
        
        self.label_ventilation.grid(row = 2,column = 2, columnspan=2)

        ##### Button states #######
        self.button_irrigation_change = customtkinter.CTkButton(master=self.frame,
                                                    text=self.__button_irrigation_text,
                                                    command=self.irrigation_change)
        self.button_irrigation_change.grid(row=3, column=0, columnspan=2)


        self.button_ventilation_change = customtkinter.CTkButton(master=self.frame,
                                                    text=self.__button_ventilation_text,
                                                    command=self.ventilation_change)
        self.button_ventilation_change.grid(row=3, column=2, columnspan=2)

         ######## TITLE 2############
        self.label_itinerario = customtkinter.CTkLabel(master=self.frame,   
                                                        text="Itinerario",
                                                        text_font=("Roboto Medium", -20))
                       
        self.label_itinerario.grid(row = 4,column = 0, sticky="",columnspan=4,pady=10)


        ####### Itineary irrigation label #########
        self.label_itinerario_irrigation = customtkinter.CTkLabel(master=self.frame,   
                                                        text="Riego\nhora inicio / hora fin ",
                                                        text_font=("Roboto Medium", -15))
                       
        self.label_itinerario_irrigation.grid(row = 5,column = 0, sticky="",columnspan=2,pady=10)

        self.label_itinerario_ventilation = customtkinter.CTkLabel(master=self.frame,   
                                                        text="Ventilación\nhora inicio / hora fin ",
                                                        text_font=("Roboto Medium", -15))
                       
        self.label_itinerario_ventilation.grid(row = 5,column = 2, sticky="",columnspan=2,pady=10)


        ### Itinerary listbox irrigation  ####
        self.list_irrigation_itinerary = tkinter.Listbox(master=self.frame,
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

        self.list_ventilation_itinerary = tkinter.Listbox(master=self.frame,
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

        self.frame_label_irrigation = customtkinter.CTkFrame(master=self.frame,
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
        
if __name__=="__main__":
    app = mainFrame()
    windows_start = control(app)
    #app.show_frame(windows_start)
    #app.hide_frame()
    app.mainloop()